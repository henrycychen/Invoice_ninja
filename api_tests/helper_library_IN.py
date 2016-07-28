import requests
import json
import random

#Use package faker factory to generate random information
from faker import Factory
faker = Factory.create()


class Generate_information(object):
    def create_name(self):
        return faker.name()

    def create_first_name(self):
        return faker.first_name()

    def create_last_name(self):
        return faker.last_name()

    def create_item(self):
        return faker.ssn()

    def create_id_num(self):
        return random.randint(1000,9999)

    def create_vat_num(self):
        return random.randint(10000,99999)

    def create_company(self):
        return faker.providers()

    def create_website(self,website=''):
        create_website = website.split(' ',1)
        return ('www.'+create_website[0]
                + create_website[1]
                + '.com').lower()

    def create_phone(self):
        phone = random.randint(1000000000,9999999999)
        return phone

    #Creates a fake name and splits the name into an email so the name
    # and email match accordingly
    def create_email(self,name=''):
        new_name = name.split(' ',1)
        return (new_name[0]
                + new_name[1]
                + '@testmail.com').lower()

    def create_street_address(self):
        street_address = str(random.randint(1,1000))\
                         + ' '+faker.first_name()\
                         + ' Street'
        return street_address

    def create_apt_suite(self):
        a_or_s = random.randint(0,1)
        if a_or_s == 0:
            a_or_s = 'Apt'
        else:
            a_or_s = 'Suite'
        create_apt_suite = a_or_s\
                           + ' ' \
                           + str(random.randint(100,999))
        return create_apt_suite

    def create_state_or_province(self):
        state_or_province = faker.first_name()
        return state_or_province[0:2].upper()

    def create_postal_code(self):
        postal_code = random.randint(10000,99999)
        return postal_code

    def create_invoice_date(self):
        invoice_date = str(random.randint(2016,2017))\
                       + '-'\
                       + str(random.randint(10,12))\
                       + '-'\
                       + str(random.randint(10,31))
        return invoice_date

    def create_partial(self):
        create_partial = random.randint(0,5)
        return create_partial

    def create_cost(self):
        create_cost = random.randint(1000,10000)
        return create_cost


class Invoice_ninja(object):
    server_ip = '104.236.192.231'
    server_api = '/api/v1/'
    invoice_ninja_clients_url = 'http://' + server_ip + server_api + 'clients'
    invoice_ninja_invoices_url = 'http://' + server_ip + server_api + 'invoices'
    invoice_ninja_payments_url = 'http://' + server_ip + server_api + 'payments'
    invoice_ninja_tasks_url = 'http://' + server_ip + server_api + 'tasks'
    get_request_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq',
                          'X-Requested-With':'XMLHttpRequest'}
    post_request_header = {'content-type': 'application/json',
                           'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq',
                           'X-Requested-With':'XMLHttpRequest'}

    def get_client(self):
        return requests.get(Invoice_ninja().invoice_ninja_clients_url,
                            headers=Invoice_ninja().get_request_header)

    def get_invoice(self):
        return requests.get(Invoice_ninja().invoice_ninja_invoices_url,
                            headers=Invoice_ninja().get_request_header)

    def post_client(self,my_data):
        return requests.post(Invoice_ninja().invoice_ninja_clients_url,
                             headers=Invoice_ninja().post_request_header,
                             data=my_data)

    def post_invoice(self,data):
        return requests.post(Invoice_ninja().invoice_ninja_invoices_url(),
                             headers=Invoice_ninja().post_request_header(),
                             data=my_data)

    #Function to create 10 clients. Should be used for new servers.
    def create_10_clients(self):
        for i in range(0,10):
            new_client = Generate_information().create_name()
            my_data = json.dumps(
                {'name':new_client, 'contact':{
                    'email': Generate_information().create_email(new_client)}})
            r = requests.post(
                Invoice_ninja().invoice_ninja_clients_url,
                headers=Invoice_ninja().post_request_header,data=my_data)

    #Function to create one client.
    def create_new_client(self,name=''):
        name = Generate_information().create_name()
        my_data = json.dumps(
            {'name': name, 'contact':{
                'email': Generate_information().create_email(name)}})
        r = requests.post(
            Invoice_ninja().invoice_ninja_clients_url,
            headers=Invoice_ninja().post_request_header,data=my_data)