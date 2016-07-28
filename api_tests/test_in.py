import pytest
import json
import requests
from helper_library_IN import *

"""
Testing the functionalities of each testable tab and API on Invoice Ninja (Client, Tasks, Invoices, and Payments). Unfortunately,
The Quotes API is the same as the Invoice API (testing the web browser Quotes tab, the data will end up under the invoices database).
Also, per the API, there isn't a POST Quotes API, only a GET, but it does not work.
"""

#Creation of some global variables to assist in creating erroneous data for testing and less coding repetition
i = Invoice_ninja()
g = Generate_information()
name = g.create_name()
id_number = g.create_id_num()
vat_number = g.create_vat_num()
website = g.create_website(name)
phone = g.create_phone()
address = g.create_street_address()
a_or_s = g.create_apt_suite()
state_province = g.create_state_or_province()
postal_code = g.create_postal_code()
email = g.split_name_to_email(name)
private_notes = g.create_item()
first_name = g.create_first_name()
last_name = g.create_last_name()
item = g.create_item
invoice_date = g.create_invoice_date()
partial = g.create_partial()
cost = g.create_cost()
qty = random.randint(5,10)
discount = random.randint(0,100)
amount = random.randint(0,3)


#Create a client by testing the available text fields under the client tab (all information created pertain to the Organizations, Address,
# and Additional Information fields)
@pytest.mark.client
def test_client_org_fields():
    my_data = json.dumps({'name':name, 'id_number':id_number, 'vat_number':vat_number, 'website':website, 'work_phone':phone,
                          'address1':address, 'address2':a_or_s, 'state':state_province, 'postal_code':postal_code,
                          'private_notes':private_notes, 'contact':{'email': email}})
    r1 = requests.post(i.invoice_ninja_clients_url, headers=i.post_request_header,data=my_data)
    r2 = i.get_client()
    check_assert = json.loads(r2.text)['data'][0]
    assert check_assert['name'] == name and \
           check_assert['id_number'] == id_number and \
           check_assert['vat_number'] == vat_number and \
           check_assert['website'] == website and \
           check_assert['work_phone'] == phone and \
           check_assert['address1'] == address and \
           check_assert['address2'] == a_or_s and \
           check_assert['state'] == state_province and \
           check_assert['postal_code'] == postal_code and \
           check_assert['private_notes'] == private_notes and \
           check_assert['contacts'][0]['email'] == email

#Create a client by testing the available text fields under Contacts
@pytest.mark.client
def test_client_contact_fields():
    email_test2 = str(first_name.lower()+last_name.lower()+'@testmail.com')
    my_data = json.dumps({'contact':{'email': email_test2, 'first_name':first_name, 'last_name':last_name,
                                     'phone':phone}})
    r1 = requests.post(i.invoice_ninja_clients_url, headers=i.post_request_header,data=my_data)
    r2 = requests.get(i.invoice_ninja_clients_url, headers=i.get_request_header)
    check_assert = json.loads(r2.text)['data'][0]['contacts'][0]
    assert check_assert['email'] == email_test2 and \
           check_assert['first_name'] == first_name and \
           check_assert['last_name'] == last_name and \
           check_assert['phone'] == phone


#Testing invoice feature by creating a new client, then generating a new invoice under that client while testing out all the
#available fields
@pytest.mark.invoices
def test_post_invoice():
    i.create_new_client
    r1 = requests.get(i.invoice_ninja_clients_url,headers=i.get_request_header)
    test_client_id = (json.loads(r1.text))['data'][0]['id']
    my_data = json.dumps({'client_id':test_client_id,'due_date': invoice_date , 'partial': partial, 'po_number' : vat_number,
                          'discount':discount,
                          'invoice_items':[{'product_key': item, 'notes': private_notes, 'cost': cost, 'qty': qty}]})
    r2 = requests.post(i.invoice_ninja_invoices_url, headers=i.post_request_header,data=my_data)
    r3 = requests.get(i.invoice_ninja_invoices_url,headers=i.get_request_header)
    check_assert = json.loads(r3.text)['data'][0]
    assert check_assert['client_id'] == test_client_id and \
           check_assert['due_date'] == invoice_date and \
           check_assert['partial'] == partial and \
           check_assert['po_number'] == vat_number and \
           check_assert['discount'] == discount and \
           check_assert['invoice_items'][0]['notes'] == private_notes and \
           check_assert['invoice_items'][0]['cost'] == cost and \
           check_assert['invoice_items'][0]['qty'] == qty and \
           check_assert['invoice_items'][0]['product_key'] == item


#Test payments tab by creating 1) creating a new client 2) using new client info to create a new invoice 3) creating a
# payment for that invoice.
@pytest.mark.payments
def test_payments():
    i.create_new_client

    r1 = requests.get(i.invoice_ninja_clients_url,headers=i.get_request_header)
    test_client_id = (json.loads(r1.text))['data'][0]['id']

    my_data = json.dumps({'client_id':test_client_id,'due_date': invoice_date , 'partial': partial, 'po_number' : vat_number,
                          'discount':discount,'invoice_items':[{'product_key': item, 'notes': private_notes, 'cost': cost, 'qty': qty}]})
    r2 = requests.post(i.invoice_ninja_invoices_url,headers=i.post_request_header,data=my_data)

    r3 = requests.get(i.invoice_ninja_invoices_url,headers=i.get_request_header)
    invoice_id = (json.loads(r3.text)['data'][0]['id'])

    my_data2 = json.dumps({'invoice_id': invoice_id, 'amount':amount, 'transaction_reference':item})
    r4 = requests.post(i.invoice_ninja_payments_url,headers=i.post_request_header,data=my_data2)

    r5 = requests.get(i.invoice_ninja_payments_url,headers=i.get_request_header)
    check_assert = json.loads(r5.text)['data'][0]
    assert check_assert['amount'] == amount and \
           check_assert['transaction_reference'] == item

#Testing the tasks by creating a new client, taking the client key and then posting a task to it.
@pytest.mark.tasks
def test_tasks():
    i.create_new_client()

    r1 = requests.get(i.invoice_ninja_tasks_url,headers=i.get_request_header)
    test_client_key = (json.loads(r1.text))['data'][0]['account_key']

    my_data = json.dumps({'account_key':test_client_key,'description':item})
    r2 = requests.post(i.invoice_ninja_tasks_url,headers=i.post_request_header,data=my_data)

    r3 = requests.get(i.invoice_ninja_tasks_url,headers=i.get_request_header)
    r3.text
    check_assert = json.loads(r3.text)['data'][0]
    assert check_assert['account_key'] == test_client_key and \
           check_assert['description'] == item


