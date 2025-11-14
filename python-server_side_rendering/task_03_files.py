#!/usr/bin/env python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_data(filename):
    """Read and return data from JSON file"""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_data(filename):
    """Read and return data from CSV file"""
    try:
        with open(filename, 'r') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
        items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)

@app.route('/products')
def display_products():
    """Route for products page - handles JSON and CSV data sources"""
    # Get query parameters from URL
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    # Load data based on source parameter
    if source == 'json':
        products = read_json_data('products.json')
    else:  # source == 'csv'
        products = read_csv_data('products.csv')
    
    # Filter by ID if provided
    if product_id:
        filtered_products = []
        for product in products:
            if str(product.get('id')) == product_id:
                filtered_products.append(product)
        
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        
        products = filtered_products
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
