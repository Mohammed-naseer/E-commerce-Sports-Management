from django import forms

STATE_CHOICES = [
   ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
    ]
CITY_CHOICES = [
    ('Ahmedabad', 'Ahmedabad'),
    ('Bangalore', 'Bangalore'),
    ('Bhopal', 'Bhopal'),
    ('Bhubaneswar', 'Bhubaneswar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chennai', 'Chennai'),
    ('Coimbatore', 'Coimbatore'),
    ('Delhi', 'Delhi'),
    ('Faridabad', 'Faridabad'),
    ('Ghaziabad', 'Ghaziabad'),
    ('Gurgaon', 'Gurgaon'),
    ('Guwahati', 'Guwahati'),
    ('Hyderabad', 'Hyderabad'),
    ('Indore', 'Indore'),
    ('Jaipur', 'Jaipur'),
    ('Jodhpur', 'Jodhpur'),
    ('Kanpur', 'Kanpur'),
    ('Kochi', 'Kochi'),
    ('Kolkata', 'Kolkata'),
    ('Lucknow', 'Lucknow'),
    ('Ludhiana', 'Ludhiana'),
    ('Madurai', 'Madurai'),
    ('Mangalore', 'Mangalore'),
    ('Mumbai', 'Mumbai'),
    ('Mysore', 'Mysore'),
    ('Nagpur', 'Nagpur'),
    ('Nashik', 'Nashik'),
    ('Noida', 'Noida'),
    ('Patna', 'Patna'),
    ('Pune', 'Pune'),
    ('Raipur', 'Raipur'),
    ('Rajkot', 'Rajkot'),
    ('Ranchi', 'Ranchi'),
    ('Surat', 'Surat'),
    ('Thane', 'Thane'),
    ('Thiruvananthapuram', 'Thiruvananthapuram'),
    ('Vadodara', 'Vadodara'),
    ('Varanasi', 'Varanasi'),
    ('Vijayawada', 'Vijayawada'),
    ('Visakhapatnam', 'Visakhapatnam'),
]



class DeliveryForm (forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    company = forms.CharField(max_length=100, required=False, label='Company')
    phoneno = forms.CharField(max_length=15, required=True, label='Phone Number')
    address_line1 = forms.CharField(max_length=255, required=True, label='Address Line 1')
    address_line2 = forms.CharField(max_length=255, required=False, label='Address Line 2')
    address_line3 = forms.CharField(max_length=255, required=False, label='Address Line 3')
    state = forms.ChoiceField(choices=STATE_CHOICES, required=True)
    city = forms.ChoiceField(choices=CITY_CHOICES, required=True)
    postalcode = forms.CharField(max_length=10, required=True, label='Zip Code')
    billing_same = forms.BooleanField(required=False, label="Use as billing address")
