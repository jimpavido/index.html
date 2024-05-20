import datetime
import random

class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Project:
    def __init__(self, customer, description, start_date, end_date, cost):
        self.customer = customer
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.cost = cost

class PaulBosackConstruction:
    def __init__(self):
        self.customers = []
        self.projects = []

    def add_customer(self, name, phone, email):
        customer = Customer(name, phone, email)
        self.customers.append(customer)
        return customer

    def add_project(self, customer, description, start_date, end_date, cost):
        project = Project(customer, description, start_date, end_date, cost)
        self.projects.append(project)
        return project

    def get_customer_by_name(self, name):
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None

    def get_project_by_customer(self, customer):
        projects = []
        for project in self.projects:
            if project.customer == customer:
                projects.append(project)
        return projects

    def get_total_project_cost(self):
        total_cost = 0
        for project in self.projects:
            total_cost += project.cost
        return total_cost

    def generate_report(self):
        report = f"Paul Bosack Construction Report\n"
        report += f"Customers:\n"
        for customer in self.customers:
            report += f"- Name: {customer.name}, Phone: {customer.phone}, Email: {customer.email}\n"
        report += f"\nProjects:\n"
        for project in self.projects:
            report += f"- Description: {project.description}, Start Date: {project.start_date.strftime('%Y-%m-%d')}, End Date: {project.end_date.strftime('%Y-%m-%d')}, Cost: ${project.cost:.2f}\n"
        report += f"\nTotal Project Cost: ${self.get_total_project_cost():.2f}"
        return report
