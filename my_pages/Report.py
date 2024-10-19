import pandas as pd
import streamlit as st
import datetime
def run_report_page(face_rec):
    


    # Function to retrieve logs from Redis
    def load_logs(name, end=-1):
        logs_list = face_rec.r.lrange(name, start=0, end=end)  # Extract all data from the Redis database
        return logs_list

    # Function to retrieve registered data
    def retrieve_registered_data():
        return face_rec.retrieve_data(name='academy:register')

    # Function to process logs and generate attendance report
    
    def generate_attendance_report():
        logs_list = load_logs(name='attendance:logs')

        # Convert logs to DataFrame
        convert_byte_to_string = lambda x: x.decode('utf-8')
        logs_list_string = list(map(convert_byte_to_string, logs_list))
        split_string = lambda x: x.split('@')
        logs_nested_list = list(map(split_string, logs_list_string))
        logs_df = pd.DataFrame(logs_nested_list, columns=['Name', 'Role', 'Timestamp'])

        # Clean and process timestamp data
        logs_df['Timestamp'] = logs_df['Timestamp'].apply(lambda x: x.split('.')[0])
        logs_df['Timestamp'] = pd.to_datetime(logs_df['Timestamp'])
        logs_df['Date'] = logs_df['Timestamp'].dt.date

        # Generate all possible date and role combinations
        all_dates = pd.date_range(start=logs_df['Date'].min(), end=logs_df['Date'].max(), freq='D').date
        registered_students = retrieve_registered_data()

        # Ensure all registered students are included in the report
        attendance_report_data = []
        for name, role in registered_students[['Name', 'Role']].values:
            for dt in all_dates:
                attendance_report_data.append({'Date': dt, 'Name': name, 'Role': role})

        # Convert to DataFrame
        attendance_report_df = pd.DataFrame(attendance_report_data)

        # Merge with logs_df to determine attendance status
        attendance_report_df = pd.merge(attendance_report_df, logs_df, how='left', on=['Date', 'Name', 'Role'])
        attendance_report_df['Status'] = attendance_report_df['Timestamp'].apply(lambda x: 'Present' if pd.notnull(x) else 'Absent')

        # Pivot table to display attendance report
        pivot_df = attendance_report_df.pivot_table(index=['Name', 'Role'], columns='Date', values='Status', aggfunc='first', fill_value='Absent')
        pivot_df = pivot_df.reset_index()
        pivot_df.index += 1
        pivot_df.index.name = 'Serial No.'

        return pivot_df
    

    # Function to filter student attendance
    def filter_student_attendance(date_in, name_in, role_in, status_in):
        logs_list = load_logs(name='attendance:logs')

        # Convert logs to DataFrame
        convert_byte_to_string = lambda x: x.decode('utf-8')
        logs_list_string = list(map(convert_byte_to_string, logs_list))
        split_string = lambda x: x.split('@')
        logs_nested_list = list(map(split_string, logs_list_string))
        logs_df = pd.DataFrame(logs_nested_list, columns=['Name', 'Role', 'Timestamp'])

        # Clean and process timestamp data
        logs_df['Timestamp'] = logs_df['Timestamp'].apply(lambda x: x.split('.')[0])
        logs_df['Timestamp'] = pd.to_datetime(logs_df['Timestamp'])
        logs_df['Date'] = logs_df['Timestamp'].dt.date

        # Generate all possible date and role combinations
        all_dates = pd.date_range(start=logs_df['Date'].min(), end=logs_df['Date'].max(), freq='D').date
        registered_students = retrieve_registered_data()

        # Ensure all registered students are included in the report
        attendance_report_data = []
        for name, role in registered_students[['Name', 'Role']].values:
            for dt in all_dates:
                attendance_report_data.append({'Date': dt, 'Name': name, 'Role': role})

        # Convert to DataFrame
        attendance_report_df = pd.DataFrame(attendance_report_data)

        # Merge with logs_df to determine attendance status
        attendance_report_df = pd.merge(attendance_report_df, logs_df, how='left', on=['Date', 'Name', 'Role'])
        attendance_report_df['Status'] = attendance_report_df['Timestamp'].apply(lambda x: 'Present' if pd.notnull(x) else 'Absent')

        # Filter based on user inputs
        filtered_df = attendance_report_df.copy()
        filtered_df['Date'] = filtered_df['Date'].astype(str)

        # Filter date
        if date_in != 'ALL':
            filtered_df = filtered_df.query(f'Date == "{date_in}"')

        # Filter name
        if name_in != 'ALL':
            filtered_df = filtered_df.query(f'Name == "{name_in}"')

        # Filter role
        if role_in != 'Student':
            filtered_df = filtered_df.query(f'Role == "{role_in}"')

        # Filter status
        if 'ALL' not in status_in:
            filtered_df = filtered_df[filtered_df['Status'].isin(status_in)]

        # Pivot table to display filtered attendance report
        pivot_df = filtered_df.pivot_table(index=['Name', 'Role'], columns='Date', values='Status', aggfunc='first', fill_value='Absent')
        pivot_df = pivot_df.reset_index()
        pivot_df.index += 1
        pivot_df.index.name = 'Serial No.'

        return pivot_df

    # Main application logic
    tab_selection = st.sidebar.radio('Select a tab:', ['Attendance Report', 'Student Search', 'Filter Students'])

    if tab_selection == 'Attendance Report':
        st.subheader('Attendance Report')
        report_df = generate_attendance_report()
        st.dataframe(report_df)

    elif tab_selection == 'Student Search':
        st.subheader('Student Search')
        st.markdown('Enter the student name to search for their attendance history:')
        student_name = st.text_input('Enter student name:')

        if st.button('Search'):
            filtered_df = filter_student_attendance(date_in='ALL', name_in=student_name, role_in='Student', status_in=['Present', 'Absent'])
            st.dataframe(filtered_df)

    elif tab_selection == 'Filter Students':
        st.subheader('Filter Students')
        st.markdown('Filter students by date, name, role, and attendance status:')

        date_in = str(st.date_input('Filter Date', datetime.datetime.now().date()))

        registered_students = retrieve_registered_data()
        name_list = registered_students['Name'].unique().tolist()
        name_in = st.selectbox('Select Name', ['ALL'] + name_list)

        role_in = 'Student'  # Default to Student role
        status_list = ['Present', 'Absent']
        status_in = st.multiselect('Select the Status', status_list, default=status_list)

        if st.button('Submit'):
            filtered_report_df = filter_student_attendance(date_in, name_in, role_in, status_in)
            st.dataframe(filtered_report_df)

