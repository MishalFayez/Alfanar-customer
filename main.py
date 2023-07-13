import streamlit as st
import pandas as pd
from streamlit_tags import st_tags
from deta import Deta
import csv
import datetime
from streamlit_custom_notification_box import custom_notification_box
import time
import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from deta import Deta
from streamlit_extras.no_default_selectbox import selectbox
from streamlit_tags import st_tags

st.set_page_config(
    page_title="Alfanar",
    page_icon=":book:",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    },layout="wide", initial_sidebar_state="expanded"

)

css = '''
[data-testid="stSidebarNav"] {
    position:absolute;
    bottom: 20%;
    color: red;
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
}
</style>
""", unsafe_allow_html=True)


st.sidebar.markdown(
    "# <span style='color:white'>Customer Registration</span> ", unsafe_allow_html=True)


deta = Deta(st.secrets["data_key"])
db = deta.Base("alfanar-customer-registeration")
db_bank = deta.Base("Bank-information")
db_workflow = deta.Base("Workflow")


data = pd.read_csv("./cr.csv", encoding="cp1252")


def list_column(column_name):
    values_list = []
    for i in range(0, data[column_name].last_valid_index() + 1):
        values_list.append(data.loc[i, column_name])
    tuple_of_numbers = tuple()

    for number in values_list:
        tuple_of_numbers += (number, )
    return tuple_of_numbers


def list_column2(column_name):
    values_list = []
    for i in range(0, data[column_name].last_valid_index() + 1):
        values_list.append(data.loc[i, column_name])
    tuple_of_numbers = tuple()

    for number in values_list:
        tuple_of_numbers += (number, )
    return tuple_of_numbers


def page_1():

    # form = st.form(key='my-form')

    # title = form.header("Initial Data")
    # with form:
    #     col1, col2 = form.columns(2)

    #     with col1:
    #         cag = st.selectbox( 'Customer Account Group', list_column('Customer Account Group'))
    #         so = st.selectbox( 'Sales Organization', list_column('Sales Organazation'))

    #     with col2:
    #         cc = st.selectbox( 'Company Code', list_column('Company Code Name'))
    #         sdc = st.selectbox( 'Sales Distribution Channel', list_column('Sales Distribution Channel'))

    # sd = form.selectbox( 'Sales Division', list_column('Sales Division'))

    # form.divider()

    # title = form.header("General Data")
    # with form:
    #     data_title = st.selectbox("Title", list_column('Title'))
    #     col1, col2 = form.columns(2)

    #     with col1:
    #         en = st.text_input("English Name", max_chars=20)
    #     with col2:
    #         ar = st.text_input("Arabic Name")
    #     search_term = st_tags(
    #         label='Search Term:',
    #         text='Press enter to add more',
    #         value=[],
    #         suggestions=[ 'six', 'seven',
    #                     'eight', 'nine', 'three',
    #                     'eleven', 'ten', 'four'],
    #         maxtags = 4,
    #         key='1')
    # form.write("##")

    # with form:
    #     col1, col2 = form.columns(2)

    #     with col1:
    #         country = st.selectbox( 'Country', list_column('Country'))
    #         region = st.selectbox( 'Region/Provice/State', list_column('Region/Province/State'))
    #     with col2:
    #         t_zone = st.selectbox( 'Transportation zone', list_column('Transportation zone'))
    #         legal_status = st.selectbox( 'Legal status', list_column('Legal status'))

    # lgt = form.text_area("Longitude")
    # form.write("##")

    # cr = form.text_input("Commercial Regestiration")
    # with form:
    #     col1, col2 = form.columns(2)

    #     with col1:
    #         cr_exdate = st.date_input("Com.Reg. Expiry date")
    #     with col2:
    #         vat = st.text_input("VAT Registration")

    # form.write("##")

    # with form:
    #     col1, col2, col3 = form.columns(3)

    #     with col1:
    #         street = st.text_input("Street/House number")
    #         b_no = st.text_input("Building Number")
    #         city = st.text_input("City")
    #     with col2:
    #         add_no = st.text_input("Additional No.(SAP Room No.)")
    #         district = st.text_input("District")
    #     with col3:
    #         po_box = st.text_input("PO Box")
    #         p_code = st.text_input("Postal Code")

    # form.write("#")

    # with form:
    #     col1, col2= form.columns(2)

    #     with col1:
    #         t_num = st.text_input("Telephone Number")
    #         m_num = st.text_input("Mobile Number")
    #     with col2:
    #         f_num = st.text_input("Fax Number")
    #         email = st.text_input("E-mail")

    # df = pd.DataFrame(
    #     columns=["Country", "Bank Key", 'Bank Account', 'Acc Holder']
    # )
    # def convert_df_to_list():
    #     pass
    # form.write('Bank Details')
    # edited_df_bank = form.data_editor(
    #     df,
    #     num_rows="dynamic",
    #     use_container_width=False,
    #     hide_index=True,
    #     column_config={
    #         "Country":st.column_config.SelectboxColumn(
    #     options=[
    #             "Saudi Arabia",
    #             "UAE",
    #             "Spain",
    #         ]
    #         )
    #     }
    #     )

    # df = pd.DataFrame(
    #     columns=["Last Name", "First Name", 'Function', 'Telephone']
    # )
    # form.write('Contact Details')
    # edited_df_contact = form.data_editor(
    #     df,
    #     key='contact',
    #     num_rows="dynamic",
    #     use_container_width=False,
    #     hide_index=True,
    #     column_config={
    #         "Function":st.column_config.SelectboxColumn(
    #     options=[
    #             "Function1",
    #             "Function2",
    #             "Function3",
    #         ]
    #         )
    #     }
    #     )
    # form.divider()

    # title = form.header("Company Code Data")
    # ra = form.text_input('Recon .Account')

    # with form:
    #     col1, col2 = form.columns(2)
    #     with col1:
    #         sk = st.text_input("Sort Key", max_chars=20)
    #     with col2:
    #         cmg = st.text_input("Cash Management Group")
    # top = form.selectbox( 'Term Of Payment', list_column('Term Of Payment '))
    # cpt = form.text_input('B/e changes payt term', disabled=True)

    # form.divider()

    # title = form.header("Sales Area Data")

    # with form:
    #     col1, col2 = form.columns(2)

    #     with col1:
    #         sale_ds = st.selectbox( 'Sales Disctrict', list_column('Sales district'))
    #         sale_o = st.selectbox( 'Sales Office', list_column('Sales Office'))
    #     with col2:
    #         sale_g = st.selectbox( 'Sales Group', list_column('Sales Group  '))
    #         customer_g = st.selectbox( 'Customer Group', list_column('Customer group'))

    # form.write('##')
    # currency = form.selectbox( 'Currency', list_column('Currency'))

    # form.write("#")

    # price_g = form.selectbox( 'Price Group', list_column('Price group'))
    # price_l = form.selectbox( 'Price List', list_column('Price List'))
    # customer_s_g = form.selectbox( 'Cust. Stats. Grp', ("1 - Material", '2 - two'))

    # form.write("#")

    # shp_c = form.selectbox( 'Shipping Conditions', list_column('Shipping Conditions'))
    # del_pl = form.selectbox( 'Delivery plant', ("MK01 - Meskan", "AP01 - Precast Factory"))
    # rfp = form.text_input('Relevant for POD')

    # form.write("#")

    # pdpi = form.selectbox( 'Partial delivery per item', list_column('Partial delivery per item'))
    # max_pd = form.text_input( 'Max. partial deliveries')

    # invoice_d = form.text_input("Invoicing dates", disabled=True)
    # invoice_l_d = form.text_input("Invoicing List Dates", disabled=True)

    # submit = form.form_submit_button('Submit')

    # if submit:
    #     #convert df to records for info
    #     bank_info = edited_df_bank.to_dict('records')
    #     contact_info = edited_df_contact.to_dict('records')

    #     res = db.fetch()
    #     all_items = res.items

    #     # Continue fetching until "res.last" is None.
    #     while res.last:
    #         res = db.fetch(last=res.last)
    #         all_items += res.items

    #     dfdb = pd.DataFrame(all_items)

    #     seq_num = ""
    #     if len(dfdb) == 0:
    #         seq_num = "RFC00001"
    #     else:
    #         value = len(dfdb)+1
    #         seq_num = "RFC" + str(value).zfill(5)

    #     now = datetime.datetime.now()

    #     created_at = now.strftime("%Y-%m-%d %H:%M:%S")

    #     #conver cr_exdate to string
    #     cr_exdate = cr_exdate.strftime("%Y-%m-%d")

    #     db.insert(
    #         {"cus_acc_g": cag,
    #         "company_code": cc,
    #         "sale_org": so,
    #         "sale_dis_ch":sdc,
    #         "sale_div": sd,
    #         "title": data_title,
    #         "eng_name": en,
    #         "ar_name": ar,
    #         "search_term": search_term,
    #         "country": country,
    #         "region": region,
    #         "t_zone": t_zone,
    #         "legal_status": legal_status,
    #         "longitude": lgt,
    #         "cr": cr,
    #         "cr_exdate": cr_exdate,
    #         "vat": vat,
    #         "street": street,
    #         "building_no": b_no,
    #         "city": city,
    #         "add_no": add_no,
    #         "district": district,
    #         "po_box": po_box,
    #         "postal_code": p_code,
    #         "tele_num": t_num,
    #         "mobile_num": m_num,
    #         "fax_num": f_num,
    #         "email": email,
    #         "raccon_acc": ra,
    #         "sort_k": sk,
    #         "cash_manag_group": cmg,
    #         "term_of_payment": top,
    #         "change_pay_term": cpt,
    #         "sales_district": sale_ds,
    #         "sales_office": sale_o,
    #         "sales_group": sale_g,
    #         "customer_group": customer_g,
    #         "currency": currency,
    #         "price_group": price_g,
    #         "price_list": price_l,
    #         "customer_stats_group": customer_s_g,
    #         "shipping_condition": shp_c,
    #         "delivery_plant": del_pl,
    #         "relevant_for_pod": rfp,
    #         "max_pd":max_pd,
    #         "invoice_dates": invoice_d,
    #         "invoice_list_dates": invoice_l_d,
    #         "bank_info":bank_info,
    #         'contact_info':contact_info,
    #         "status":"Pending",
    #         'created_at': created_at},
    #         seq_num)

    #     progress_bar = st.progress(0)

    #     for perc_completed in range(100):
    #         time.sleep(0.020)
    #         progress_bar.progress(perc_completed+1)

    #     st.success("Record : "+ seq_num+ " is registered successfully!")

    deta = Deta(st.secrets["data_key"])
    db = deta.Base("alfanar-customer-registeration")
    db_bank = deta.Base("Bank-information")
    db_workflow = deta.Base("Workflow")

    data = pd.read_csv("./cr.csv", encoding="cp1252")

    def list_column(column_name):
        values_list = []
        for i in range(0, data[column_name].last_valid_index() + 1):
            values_list.append(data.loc[i, column_name])
        tuple_of_numbers = tuple()

        for number in values_list:
            tuple_of_numbers += (number, )
        return tuple_of_numbers

    if 'current_view' not in st.session_state:
        st.session_state['current_view'] = 'Grid'

    if 'current_step' not in st.session_state:
        st.session_state['current_step'] = 1

    def set_page_view(page):
        st.session_state['current_view'] = page
        st.session_state['current_step'] = 1

    def set_form_step(action, step=None, *args, **kwargs):
        if action == 'Next':
            st.session_state['current_step'] = st.session_state['current_step'] + 1
        if action == 'Back':
            st.session_state['current_step'] = st.session_state['current_step'] - 1
        if action == 'Jump':
            st.session_state['current_step'] = step

    ##### wizard functions ####

    def wizard_form_header():
        sf_header_cols = st.columns([1, 1.75, 1])

        with sf_header_cols[1]:
            st.subheader('Customer Registeration')

        # determines button color which should be red when user is on that given step
        wh_type = 'primary' if st.session_state['current_step'] == 1 else 'secondary'
        ff_type = 'primary' if st.session_state['current_step'] == 2 else 'secondary'
        lo_type = 'primary' if st.session_state['current_step'] == 3 else 'secondary'
        sf_type = 'primary' if st.session_state['current_step'] == 4 else 'secondary'

        step_cols = st.columns([.05, 1.5, 1.5, 2, 1.5, .05])
        step_cols[1].button('Initial Data', on_click=set_form_step, args=[
                            'Jump', 1], type=wh_type)
        step_cols[2].button('General Data', on_click=set_form_step, args=[
                            'Jump', 2], type=ff_type)
        step_cols[3].button('Company Code Data', on_click=set_form_step, args=[
                            'Jump', 3], type=lo_type)
        step_cols[4].button('Sales Area Data', on_click=set_form_step, args=[
                            'Jump', 4], type=sf_type)

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
        if (st.session_state['current_step']) == 1:
            col1, col2 = st.columns(2)

            with col1:
                cag = st.selectbox('Customer Account Group', list_column(
                    'Customer Account Group'), index=default_value_index(list_column('Customer Account Group'), "cag"))
                st.session_state.cag = cag
                so = st.selectbox('Sales Organization', list_column(
                    'Sales Organazation'), index=default_value_index(list_column('Sales Organazation'), "so"))
                st.session_state.so = so
            with col2:
                cc = st.selectbox('Company Code', list_column(
                    'Company Code Name'), index=default_value_index(list_column('Company Code Name'), "cc"))
                st.session_state.cc = cc
                sdc = st.selectbox('Sales Distribution Channel', list_column(
                    'Sales Distribution Channel'), index=default_value_index(list_column('Sales Distribution Channel'), "sdc"))
                st.session_state.sdc = sdc

            sd = st.selectbox('Sales Division', list_column(
                'Sales Division'), index=default_value_index(list_column('Sales Division'), "sd"))
            st.session_state.sd = sd
        elif (st.session_state['current_step']) == 2:
            col1, col2, col3 = st.columns(3)
            title = col1.selectbox("Title", list_column(
                'Title'), index=default_value_index(list_column('Title'), "title"))
            st.session_state.title = title
            eng_name = col2.text_input(
                "English Name", max_chars=20, value=text_value("eng_name"))
            st.session_state.eng_name = eng_name
            ar_name = col3.text_input(
                "Arabic Name", value=text_value("ar_name"))
            st.session_state.ar_name = ar_name
            search_term = st_tags(
                label='Search Term:',
                text='Press enter to add more',
                value=[],
                suggestions=['six', 'seven',
                             'eight', 'nine', 'three',
                             'eleven', 'ten', 'four'],
                maxtags=4,
                key='1')
            st.session_state.search_term = str(search_term)
            country = col1.selectbox('Country', list_column(
                'Country'), index=default_value_index(list_column('Country'), "Country"))
            st.session_state.country = country
            region = col2.selectbox('Region/Provice/State', list_column('Region/Province/State'),
                                    index=default_value_index(list_column('Region/Province/State'), "region"))
            st.session_state.region = region
            t_zone = col3.selectbox('Transportation zone', list_column(
                'Transportation zone'), index=default_value_index(list_column('Transportation zone'), "t_zone"))
            st.session_state.t_zone = t_zone

            gd_cols = st.columns([1, 2])
            with gd_cols[0]:
                legal = st.selectbox('Legal status', list_column(
                    'Legal status'), index=default_value_index(list_column('Legal status'), "legal"))
                st.session_state.legal = legal
            with gd_cols[1]:
                longitude = st.text_area(
                    "Longitude", value=text_value("longitude"))
                st.session_state.longitude = longitude

            col1, col2, col3 = st.columns(3)
            with col1:
                cr = st.text_input("Commercial Regestiration",
                                   value=text_value("cr"))
                st.session_state.cr = cr
            with col2:
                cr_exdate = st.date_input("Com.Reg. Expiry date")
                st.session_state.cr_exdate = cr_exdate
            with col3:
                vat = st.text_input("VAT Registration",
                                    value=text_value("vat"))
                st.session_state.vat = vat

            col1, col2, col3 = st.columns(3)
            with col1:
                street = st.text_input(
                    "Street/House number", value=text_value("street"))
                st.session_state.street = street
                b_no = st.text_input(
                    "Building Number", value=text_value("b_no"))
                st.session_state.b_no = b_no
                city = st.text_input("City", value=text_value("city"))
                st.session_state.city = city
            with col2:
                add_no = st.text_input(
                    "Additional No.(SAP Room No.)", value=text_value("add_no"))
                st.session_state.add_no = add_no
                district = st.text_input(
                    "District", value=text_value("district"))
                st.session_state.district = district
            with col3:
                po_box = st.text_input("PO Box", value=text_value("po_box"))
                st.session_state.po_box = po_box
                p_code = st.text_input(
                    "Postal Code", value=text_value("p_code"))
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

            col1, col2, col3 = st.columns([1, 1.05, 0.5])
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
                        "Country": st.column_config.SelectboxColumn(
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
            col1, col2, col3 = st.columns([1, 1.05, 0.5])

            with col2:
                st.text('Contact Details')
            with col3:
                save_bank = st.button(
                    'Save Contact', on_click=save_edit_contact)
            st.session_state.edited_df_contact = st.data_editor(
                df_contact,
                key='contact',
                num_rows="dynamic",
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Function": st.column_config.SelectboxColumn(
                        options=[
                            "Function1",
                            "Function2",
                            "Function3",
                        ]
                    )
                }
            )

        elif (st.session_state['current_step']) == 3:

            col1, col2 = st.columns(2)
            with col1:
                ra = st.text_input('Recon .Account', value=text_value("ra"))
                st.session_state.ra = ra
                cmg = st.text_input("Cash Management Group",
                                    value=text_value("cmg"))
                st.session_state.cmg = cmg
            with col2:
                top = st.selectbox('Term Of Payment', list_column(
                    'Term Of Payment '), index=default_value_index(list_column('Term Of Payment '), "top"))
                st.session_state.top = top
                cpt = st.text_input('B/e changes payt term',
                                    disabled=True, value=' ')
                st.session_state.cpt = cpt
        elif (st.session_state['current_step']) == 4:

            col1, col2, col3 = st.columns(3)

            with col1:
                sale_ds = st.selectbox('Sales Disctrict', list_column(
                    'Sales district'), index=default_value_index(list_column('Sales district'), "sale_ds"))
                st.session_state.sale_ds = sale_ds
                sale_o = st.selectbox('Sales Office', list_column(
                    'Sales Office'), index=default_value_index(list_column('Sales Office'), "sale_o"))
                st.session_state.sale_o = sale_o
                price_g = st.selectbox('Price Group', list_column(
                    'Price group'), index=default_value_index(list_column('Price group'), "price_g"))
                st.session_state.price_g = price_g
                price_l = st.selectbox('Price List', list_column(
                    'Price List'), index=default_value_index(list_column('Price List'), "price_l"))
                st.session_state.price_l = price_l
                # customer_s_g = st.selectbox( 'Cust. Stats. Grp', ("1 - Material", '2 - two'), index=default_value_index(["1 - Material", '2 - two'], "customer_s_g"))
            with col2:
                sale_g = st.selectbox('Sales Group', list_column(
                    'Sales Group  '), index=default_value_index(list_column('Sales Group  '), "sale_g"))
                st.session_state.sale_g = sale_g
                customer_g = st.selectbox('Customer Group', list_column(
                    'Customer group'), index=default_value_index(list_column('Customer group'), "customer_g"))
                st.session_state.customer_g = customer_g
                shp_c = st.selectbox('Shipping Conditions', list_column(
                    'Shipping Conditions'), index=default_value_index(list_column('Shipping Conditions'), "shp_c"))
                st.session_state.shp_c = shp_c
                # del_pl = st.selectbox( 'Delivery plant', ("MK01 - Meskan", "AP01 - Precast Factory"))
                rfp = st.text_input('Relevant for POD',
                                    value=text_value("rfp"))
                st.session_state.rfp = rfp
            with col3:
                currency = st.selectbox('Currency', list_column(
                    'Currency'), index=default_value_index(list_column('Currency'), "currency"))
                st.session_state.currency = currency
                pdpi = st.selectbox('Partial delivery per item', list_column(
                    'Partial delivery per item'), index=default_value_index(list_column('Partial delivery per item'), "pdpi"))
                st.session_state.pdpi = pdpi
                max_pd = st.text_input(
                    'Max. partial deliveries', value=text_value("max_pd"))
                st.session_state.max_pd = max_pd
                invoice_d = st.text_input(
                    "Invoicing dates", disabled=True, value=text_value("invoice_d"))
                st.session_state.invoice_d = invoice_d
                invoice_l_d = st.text_input(
                    "Invoicing List Dates", disabled=True, value=text_value("invoice_l_d"))
                st.session_state.invoice_l_d = invoice_l_d

            st.file_uploader("Upload File", type=['csv', 'xlsx'], accept_multiple_files=True, key='upload_file')

    def wizard_form_footer():
        form_footer_container = st.empty()
        with form_footer_container.container():

            disable_back_button = True if st.session_state['current_step'] == 1 else False
            disable_next_button = True if st.session_state['current_step'] == 4 else False
            disable_submit_button = True if st.session_state['current_step'] != 4 else False

            form_footer_cols = st.columns([5, 1, 1, 1.75])

            form_footer_cols[1].button('Back', on_click=set_form_step, args=[
                                       'Back'], disabled=disable_back_button)
            form_footer_cols[2].button('Next', on_click=set_form_step, args=[
                                       'Next'], disabled=disable_next_button)
            submit = form_footer_cols[3].button(
                'Submit', disabled=disable_submit_button)
            if submit:
                if 'edited_df_bank' in st.session_state:
                    bank_info = st.session_state.edited_df_bank.to_dict(
                        'records')
                if 'edited_df_contact' in st.session_state:
                    contact_info = st.session_state.edited_df_contact.to_dict(
                        'records')

                res = db.fetch()
                all_items = res.items

                # Continue fetching until "res.last" is None.
                while res.last:
                    res = db.fetch(last=res.last)
                    all_items += res.items

                dfdb = pd.DataFrame(all_items)
                seq_num = ""
                if len(dfdb) == 0:
                    seq_num = "RFC00001"
                else:
                    value = len(dfdb)+1
                    seq_num = "RFC" + str(value).zfill(5)

                now = datetime.datetime.now()

                created_at = now.strftime("%Y-%m-%d %H:%M:%S")

                # conver cr_exdate to string
                # cr_exdate = cr_exdate.strftime("%Y-%m-%d")
                # st.dataframe(pd.DataFrame({'company': 'FA11 - Alfanar Dubai Manufacturi', 'key': 'app-fa11-group', 'status_name': 'Pending for approval', 'workflow': [{'name': 'Sami', 'status': 'Pending'}]}, {'company': 'FA11 - Alfanar Dubai Manufacturi', 'key': 'app-fa11-group', 'status_name': 'Final Approve Done', 'workflow': [{'name': 'Abdullah', 'status': "Didn't receive'"}]})['workflow'])
                if st.session_state.cc == "FA10 - Alfanar AED":
                    status_workflow = {'company': 'FA10 - Alfanar AED', 'key': 'app-fa10-group', 'status_name': 'Pending for approval', 'workflow': [{'name': 'Ibrahim', 'status': 'Pending'}, {'name': 'Amjad', 'status': 'Pending'}]}, {'company': 'FA10 - Alfanar AED', 'key': 'app-fa10-group', 'status_name': 'Final Approve Done', 'workflow': [{'name': 'Hossam', 'status': "Didn't receive'"}, {'name': 'Ahmed', 'status': "Didn't receive"}]},
                else:
                    status_workflow = {'company': 'FA11 - Alfanar Dubai Manufacturi', 'key': 'app-fa11-group', 'status_name': 'Pending for approval', 'workflow': [{'name': 'Sami', 'status': 'Pending'}]}, {'company': 'FA11 - Alfanar Dubai Manufacturi', 'key': 'app-fa11-group', 'status_name': 'Final Approve Done', 'workflow': [{'name': 'Abdullah', 'status': "Didn't receive'"}]},

                db.insert(
                    {"cus_acc_g": st.session_state.cag,
                     "company_code": st.session_state.cc,
                     "sale_org": st.session_state.so,
                     "sale_dis_ch": st.session_state.sdc,
                     "sale_div": st.session_state.sd,
                     "title": st.session_state.title,
                     "eng_name": st.session_state.eng_name,
                     "ar_name": st.session_state.ar_name,
                     "search_term": st.session_state.search_term,
                     "country": st.session_state.country,
                     "region": st.session_state.region,
                     "t_zone": st.session_state.t_zone,
                     "legal_status": st.session_state.legal,
                     "longitude": st.session_state.longitude,
                     "cr": st.session_state.cr,
                     # "cr_exdate": st.session_state.cr_exdate,
                     "vat": st.session_state.vat,
                     "street": st.session_state.street,
                     "building_no": st.session_state.b_no,
                     "city": st.session_state.city,
                     "add_no": st.session_state.add_no,
                     "district": st.session_state.district,
                     "po_box": st.session_state.po_box,
                     "postal_code": st.session_state.p_code,
                     "raccon_acc": st.session_state.ra,
                     # "sort_k": st.session_state.search_term,
                     "cash_manag_group": st.session_state.cmg,
                     "term_of_payment": st.session_state.top,
                     "change_pay_term": st.session_state.cpt,
                     "sales_district": st.session_state.sale_ds,
                     "sales_office": st.session_state.sale_o,
                     "sales_group": st.session_state.sale_g,
                     "customer_group": st.session_state.customer_g,
                     "currency": st.session_state.currency,
                     "price_group": st.session_state.price_g,
                     "price_list": st.session_state.price_l,
                     # "customer_stats_group": customer_s_g,
                     "shipping_condition": st.session_state.shp_c,
                     # "delivery_plant": del_pl,
                     "relevant_for_pod": st.session_state.rfp,
                     "max_pd": st.session_state.max_pd,
                     "invoice_dates": st.session_state.invoice_d,
                     "invoice_list_dates": st.session_state.invoice_l_d,
                     "bank_info": bank_info,
                     'contact_info': contact_info,
                     "status": "Pending for Approved",
                     'status_workflow':status_workflow,
                        'created_at': created_at},
                    seq_num)
                progress_bar = st.progress(0)

                for perc_completed in range(100):
                    time.sleep(0.020)
                    progress_bar.progress(perc_completed+1)

                st.success("Record : " + seq_num +
                           " is registered successfully!")

    ### Replace Render Wizard View With This ###

    def render_wizard_view():
        with st.expander('', expanded=True):
            wizard_form_header()

            wizard_form_body()

            wizard_form_footer()

    render_wizard_view()


if __name__ == "__main__":
    page_1()
