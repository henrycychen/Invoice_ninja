import requests
import json
import random
#Use package faker factory to generate random information
from faker import Faker
faker = Faker()

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
        phone1 = str(random.randint(100,999))
        phone2 = str(random.randint(100,999))
        phone3 = str(random.randint(1000,9999))
        final_phone = phone1+"-"+phone2+"-"+phone3
        return final_phone

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
