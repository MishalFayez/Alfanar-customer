import streamlit as st
import pandas as pd
from streamlit_tags import st_tags
from deta import Deta
import time
import streamlit.components.v1 as components
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode, GridUpdateMode,AgGridTheme
from annotated_text import annotated_text, annotation, parameters
import datetime
from streamlit_extras.stoggle import stoggle
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode



st.set_page_config(
    page_title="Alfanar",
    page_icon=":book:",
    menu_items={
    'Get Help': 'https://www.extremelycoolapp.com/help',
    'Report a bug': "https://www.extremelycoolapp.com/bug",
    'About': "# This is a header. This is an *extremely* cool app!"
},layout="wide", initial_sidebar_state="expanded"

)

css='''
[data-testid="stSidebarNav"] {
    position:absolute;
    bottom: 20%;
    color: blue;
    color:white
}
'''

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
st.sidebar.image("new.png")
st.sidebar.divider()
st.markdown("""
<style>
[data-testid=stSidebar] {
  background-color: #2d5d9f;
  color: white;
  .ag-row-selected A {
  color: while;
}
}
</style>
""", unsafe_allow_html=True)



st.sidebar.markdown("# <span style='color:white'>Customer Registration</span> ", unsafe_allow_html=True)


deta = Deta(st.secrets["data_key"])
db = deta.Base("alfanar-customer-registeration")
db_bank = deta.Base("Bank-information")


def page_1():

    res = db.fetch()
    all_items = res.items

    # Continue fetching until "res.last" is None.
    while res.last:
        res = db.fetch(last=res.last)
        all_items += res.items
    # df = pd.read_table(all_items)
    df = pd.DataFrame(all_items, columns=['key','cr', "eng_name",'company_code', 'status', 'created_at'])


    gb = GridOptionsBuilder.from_dataframe(df)

    #customization
    gb.configure_default_column(
        groupable=True,
        value = True, )
    gb.configure_column(
        "eng_name",
        header_name="English Name")
    gb.configure_column(
        "cr",
        header_name="CR"
    )
    gb.configure_column(
    field="company_code", header_name="Company Code", tooltipField="Company number"
    )
    gb.configure_column(
    field="key", header_name="Sequence Number", tooltipField="Sequence Number"
    )
    gb.configure_selection(selection_mode='single', use_checkbox=True)

    gb.configure_grid_options(tooltipShowDelay=0)

    gridOptions = gb.build()


    grid_response = AgGrid(
    df, 
    gridOptions=gridOptions,
    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,

    width='100%',
    data_return_mode='FILTERED', 
    update_mode='GRID_CHANGED',
    fit_columns_on_grid_load=False,
    theme=AgGridTheme.ALPINE,
    # custom_css={".ag-row-hover": {"background-color": "lightblue !important"},
    # ".ag-row-selected": {"background-color": "lightblue !important"},
    # ".ag-cell-range-selected:not(.ag-cell-focus)": {"background-color": "lightblue !important"}
    
    # },
    allow_unsafe_jscode=True, #Set it to True to allow jsfunction to be injected
    
    )
    data = pd.read_csv("./cr.csv", encoding="cp1252")
    def list_column(column_name):
        values_list = []
        for i in range(0, data[column_name].last_valid_index() + 1):
            values_list.append(data.loc[i, column_name])
        tuple_of_numbers = tuple()

        for number in values_list:
            tuple_of_numbers += (number, )
        return tuple_of_numbers

    if grid_response["selected_rows"]:
        sel_row = grid_response["selected_rows"]
        st.session_state['sel_row'] = sel_row[0]["key"]
        sel_df = pd.DataFrame(sel_row)


        record_selected = db.get(sel_df['key'][0])


        if 'current_view' not in st.session_state:
            st.session_state['current_view'] = 'Grid'

        if 'current_step' not in st.session_state:
            st.session_state['current_step'] = 1


        def set_page_view(page):
            st.session_state['current_view'] = page
            st.session_state['current_step'] = 1         

        def set_form_step(action,step=None, *args, **kwargs):
            if action == 'Next':
                st.session_state['current_step'] = st.session_state['current_step'] + 1
            if action == 'Back':
                st.session_state['current_step'] = st.session_state['current_step'] - 1
            if action == 'Jump':
                st.session_state['current_step'] = step


        ##### wizard functions ####
        def wizard_form_header():
            sf_header_cols = st.columns([1,1.75,1])
                
            with sf_header_cols[1]:            
                st.subheader('Customer Registeration')
                    
            # determines button color which should be red when user is on that given step
            wh_type = 'primary' if st.session_state['current_step'] == 1 else 'secondary'
            ff_type = 'primary' if st.session_state['current_step'] == 2 else 'secondary'
            lo_type = 'primary' if st.session_state['current_step'] == 3 else 'secondary'
            sf_type = 'primary' if st.session_state['current_step'] == 4 else 'secondary'

            step_cols = st.columns([.05,1.5,1.5,2,1.5,.05])    
            step_cols[1].button('Initial Data',on_click=set_form_step,args=['Jump',1],type=wh_type)
            step_cols[2].button('General Data',on_click=set_form_step,args=['Jump',2],type=ff_type)        
            step_cols[3].button('Company Code Data',on_click=set_form_step,args=['Jump',3],type=lo_type)      
            step_cols[4].button('Sales Area Data',on_click=set_form_step,args=['Jump',4],type=sf_type)

        def default_value_index(tuple, session_name):
            if session_name not in st.session_state:
                default_ix = 0
            else:
                # st.session_state[session_name] = tuple
                default_ix = tuple.index(st.session_state[session_name])
                
            return default_ix

        def text_value(session_name):
            if session_name not in st.session_state:
                default_value = ''
            else:
                default_value = st.session_state[session_name]

            return default_value


        ### Replace Wizard Form Body with this ###
        def wizard_form_body():
            if(st.session_state['current_step']) == 1:
                col1, col2 = st.columns(2)
                
                with col1:
                    cag = st.text_input( 'Customer Account Group', value=record_selected['cus_acc_g'], disabled=True)
                    st.session_state.cag = cag
                    so = st.selectbox( 'Sales Organization', list_column('Sales Organazation'),index=default_value_index(list_column('Sales Organazation'), "so"))
                    st.session_state.so = so
                with col2:
                    cc = st.selectbox( 'Company Code', list_column('Company Code Name'),index=default_value_index(list_column('Company Code Name'), "cc"))
                    st.session_state.cc = cc
                    sdc = st.selectbox( 'Sales Distribution Channel', list_column('Sales Distribution Channel'),index=default_value_index(list_column('Sales Distribution Channel'), "sdc"))
                    st.session_state.sdc = sdc

                sd = st.selectbox( 'Sales Division', list_column('Sales Division'),index=default_value_index(list_column('Sales Division'), "sd"))
                st.session_state.sd = sd
            elif (st.session_state['current_step']) == 2:
                col1, col2, col3 = st.columns(3)
                title = col1.selectbox("Title", list_column('Title'),index=default_value_index(list_column('Title'), "title"))
                st.session_state.title = title
                eng_name = col2.text_input("English Name", max_chars=20, value=text_value("eng_name"))
                st.session_state.eng_name = eng_name
                ar_name = col3.text_input("Arabic Name", value=text_value("ar_name"))
                st.session_state.ar_name = ar_name
                search_term = st_tags(
                    label='Search Term:',
                    text='Press enter to add more',
                    value=[],
                    suggestions=[ 'six', 'seven', 
                                'eight', 'nine', 'three', 
                                'eleven', 'ten', 'four'],
                    maxtags = 4,
                key='1')
                st.session_state.search_term = str(search_term)
                country = col1.selectbox( 'Country', list_column('Country'),index=default_value_index(list_column('Country'), "Country"))
                st.session_state.country = country
                region = col2.selectbox( 'Region/Provice/State', list_column('Region/Province/State'),index=default_value_index(list_column('Region/Province/State'), "region"))
                st.session_state.region = region
                t_zone = col3.selectbox( 'Transportation zone', list_column('Transportation zone'),index=default_value_index(list_column('Transportation zone'), "t_zone"))
                st.session_state.t_zone = t_zone

                gd_cols = st.columns([1,2])
                with gd_cols[0]:
                    legal = st.selectbox( 'Legal status', list_column('Legal status'),index=default_value_index(list_column('Legal status'), "legal"))
                    st.session_state.legal = legal
                with gd_cols[1]:
                    longitude = st.text_area("Longitude", value=text_value("longitude"))
                    st.session_state.longitude = longitude

                col1,col2,col3 = st.columns(3)
                with col1:
                    cr = st.text_input("Commercial Regestiration", value=text_value("cr"))
                    st.session_state.cr = cr
                with col2:
                    cr_exdate = st.date_input("Com.Reg. Expiry date")
                    st.session_state.cr_exdate = cr_exdate
                with col3:
                    vat = st.text_input("VAT Registration", value=text_value("vat"))
                    st.session_state.vat = vat

                col1, col2, col3 = st.columns(3)    
                with col1:
                    street = st.text_input("Street/House number", value=text_value("street"))
                    st.session_state.street = street
                    b_no = st.text_input("Building Number", value=text_value("b_no"))
                    st.session_state.b_no = b_no
                    city = st.text_input("City", value=text_value("city"))
                    st.session_state.city = city
                with col2:
                    add_no = st.text_input("Additional No.(SAP Room No.)", value=text_value("add_no"))
                    st.session_state.add_no = add_no
                    district = st.text_input("District", value=text_value("district"))
                    st.session_state.district = district
                with col3:
                    po_box = st.text_input("PO Box", value=text_value("po_box"))
                    st.session_state.po_box = po_box
                    p_code = st.text_input("Postal Code", value=text_value("p_code"))
                    st.session_state.p_code = p_code

                
                

                if 'df_bank' not in st.session_state:
                    st.session_state.df_bank = pd.DataFrame({
                        "Country": [''], 
                        "Bank Key": [''],
                        "Bank Account": [''],
                        "Account Holder": ['']
                        }
                    )
                    st.session_state.edited_df_bank = st.session_state.df_bank.copy()

        

                def save_edit_bank():
                    st.session_state.df_bank = st.session_state.edited_df_bank.copy()


                col1, col2, col3 = st.columns([1,1.05,0.5])
                with col2:
                    st.text('Bank Details')
                with col3:
                    save_bank = st.button('Save Bank', on_click=save_edit_bank)


                df_bank = st.session_state.df_bank
                def funct1_bank():
                    st.session_state.edited_df_bank = st.data_editor(
                        df_bank,
                        num_rows="dynamic",
                        use_container_width=True,
                        hide_index=True,
                        column_config={
                            "Country":st.column_config.SelectboxColumn(
                        options=[
                                "Saudi Arabia",
                                "UAE",
                                "Spain",
                            ]
                            )
                        }
                    )
                    return
                funct1_bank()
                


                if 'df_contact' not in st.session_state:
                    st.session_state.df_contact = pd.DataFrame(
                        # columns=["First Name","Last Name", 'Function', 'Telephone']
                        {
                        "First Name": [''], 
                        "Last Name": [''],
                        "Function": [''],
                        "Telephone": ['']
                        }
                        )
                    st.session_state.edited_df_contact = st.session_state.df_contact.copy()

                def save_edit_contact():
                    st.session_state.df_contact = st.session_state.edited_df_contact.copy()


                df_contact = st.session_state.df_contact
                col1, col2, col3 = st.columns([1,1.05,0.5])

                with col2:
                    st.text('Contact Details')
                with col3:
                    save_bank = st.button('Save Contact', on_click=save_edit_contact)
                st.session_state.edited_df_contact = st.data_editor(
                    df_contact,
                    key='contact',
                    num_rows="dynamic",
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "Function":st.column_config.SelectboxColumn(
                    options=[
                            "Function1",
                            "Function2",
                            "Function3",
                        ]
                        )
                    }
                )

                

                
            elif (st.session_state['current_step']) == 3:

                col1,col2 = st.columns(2)
                with col1:
                    ra = st.text_input('Recon .Account')
                    cmg = st.text_input("Cash Management Group")
                with col2:
                    top = st.selectbox( 'Term Of Payment', list_column('Term Of Payment '))
                    cpt = st.text_input('B/e changes payt term', disabled=True)
            elif (st.session_state['current_step']) == 4:

                
                col1,col2,col3 = st.columns(3)

                with col1:
                    sale_ds = st.selectbox( 'Sales Disctrict', list_column('Sales district'))
                    sale_o = st.selectbox( 'Sales Office', list_column('Sales Office'))
                    price_g = st.selectbox( 'Price Group', list_column('Price group'))
                    price_l = st.selectbox( 'Price List', list_column('Price List'))
                    customer_s_g = st.selectbox( 'Cust. Stats. Grp', ("1 - Material", '2 - two'))
                with col2:
                    sale_g = st.selectbox( 'Sales Group', list_column('Sales Group  '))
                    customer_g = st.selectbox( 'Customer Group', list_column('Customer group'))
                    shp_c = st.selectbox( 'Shipping Conditions', list_column('Shipping Conditions'))
                    del_pl = st.selectbox( 'Delivery plant', ("MK01 - Meskan", "AP01 - Precast Factory"))
                    rfp = st.text_input('Relevant for POD')
                with col3:
                    currency = st.selectbox( 'Currency', list_column('Currency'))
                    pdpi = st.selectbox( 'Partial delivery per item', list_column('Partial delivery per item'))
                    max_pd = st.text_input( 'Max. partial deliveries')
                    invoice_d = st.text_input("Invoicing dates", disabled=True)
                    invoice_l_d = st.text_input("Invoicing List Dates", disabled=True)

                

        def wizard_form_footer():    
            form_footer_container = st.empty()
            with form_footer_container.container():
                
                disable_back_button = True if st.session_state['current_step'] == 1 else False
                disable_next_button = True if st.session_state['current_step'] == 4 else False
                
                form_footer_cols = st.columns([5,1,1,1.75])
                

                form_footer_cols[1].button('Back',on_click=set_form_step,args=['Back'],disabled=disable_back_button)
                form_footer_cols[2].button('Next',on_click=set_form_step,args=['Next'],disabled=disable_next_button)
            
                

        ### Replace Render Wizard View With This ###
        def render_wizard_view():
            with st.expander('',expanded=True):
                wizard_form_header()

                wizard_form_body()

                wizard_form_footer()

        render_wizard_view()
        df_record_selected = pd.DataFrame.from_dict(record_selected, orient='index')
        with st.expander('',expanded=True):

            col1, col2 = st.columns(2)
            with col1:
                if df_record_selected[0]['status_workflow'][0]['company'] == df_record_selected[0]['company_code']:
                    st.write( 'Current Workflow (', df_record_selected[0]['status_workflow'][0]['status_name'],')')
                    try:
                        df_workflow_current = pd.DataFrame.from_dict(df_record_selected[0]['status_workflow'][0]['workflow'], orient='index').transpose()
                        st.dataframe(df_workflow_current, use_container_width=True, hide_index=True)
                    except:
                        for i in df_record_selected[0]['status_workflow'][0]['workflow']:
                            st.dataframe(pd.DataFrame.from_dict(i, orient='index').transpose(), use_container_width=True, hide_index=True)
            with col2:
                if df_record_selected[0]['status_workflow'][1]['company'] == df_record_selected[0]['company_code']:
                    st.write( 'Next Workflow (', df_record_selected[0]['status_workflow'][1]['status_name'],')')
                    try:
                        df_workflow_next = pd.DataFrame.from_dict(df_record_selected[0]['status_workflow'][1]['workflow'], orient='index').transpose()
                        st.dataframe(df_workflow_next, use_container_width=True, hide_index=True)
                    except:
                        for i in df_record_selected[0]['status_workflow'][1]['workflow']:
                            st.dataframe(pd.DataFrame.from_dict(i, orient='index').transpose(), use_container_width=True, hide_index=True)


        form = st.form(key="my--form")

        status_form = form.selectbox( 'Change Status', ("Approved", "Reject & close", "Reject & send back"))
        note_form = form.text_area('Note', height=100)
        att_form = form.file_uploader('Attachment')
        submit = form.form_submit_button('Submit')

        if submit:
            # db.update({"status" : status_form}, record_selected['key'])

            st.empty()

            st.write("Good")
 

if __name__ == "__main__":
    page_1()