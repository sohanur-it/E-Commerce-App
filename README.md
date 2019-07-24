# E-Comerce-Application (Django)
<h4>
##Create a superUser account before interacting with User, Account, Model and Admin Privilages
</h4>
<h2>
Main Features :
</h2>
        
<ul>
        <li>Full Featured E-Commerce Application Product and Custom Post</li>
        <li>DetailView of Each Product With ADD/REMOVE Cart Facilities</li>
        <li>Custom Admin Panel </li>
        <li>Order Summary with total bill</li>
        <li>Checkout View with Product List</li>
        <li>Discount cupon Option for product</li>
        <li>Payment Option Stripe/Paypal</li>
        <li>Stripe Api Customization</li>
        <li>Category Based Product with price, title and image and others attributes </li>
        <li>Automatic and Unique Slug Generator for each product</li>
        <li>Slug Based URL For SEO Friendly</li>
        <li>User Profile Page with Update Feature</li>
        <li>Registration,Login,Logout Page</li>
        <li>Frondend and Backend Validation</li>
        <li>Classbased Listview, DetailView, CreateView, UpdateView, DeleteView </li>
        <li>After Login, User can update Their Profile Info Like (E-mail , Username and Profile Pictures) </li>
  
  </ul>

<h2>
Used Technolgies :
</h2>
<ul>
<li>Python</li>
<li>Django v2.2.3</li>
<li>Jquery</li>
<li>Stripe Api</li>
<li>SQLite3</li>
<li>HTML</li>
<li>CSS</li>
<li>Bootstrap</li>
<li>Crispy Form</li>
<li>Font-Awesome</li>
<li>JavaScript</li>
</ul>

<h2>Installation</h2>
<h4>Create djecom virtual environment & goto the directory.
</h4>

<h2>@Linux:</h2>

```virtual
virtualenv -p /usr/bin/python3 djecom 
cd djecom
```

<h2> @Windows : </h2>

```windows
virtualenv djecom
cd .\djecom\
```

<h2> Activate virtualenv : </h2>

```activate
source bin/activate
```

<h2> @ For Windows: </h2>

```windows
.\Scripts\activate
```

<h2> Clone the project in the djecom directory </h2>

```clone
git clone https://github.com/sohanur-it/E-Comerce-App.git
```

<h2> Setup </h2>

```move
mv E-Comerce-App src/    
mv src/requirements.txt . 
```

<h2>Install requirements.txt </h2>

```install
python -m pip install -r requirement.txt
```


<h4>Warning: In case it show's error install django first in the system / error (pkg-resources==0.0.0)--Just remove the line from requirement.txt file / install the packages manually /  </h4>

```install
pip install django
pip install --upgrade -r requirement.txt
```

<h2> Now goto src/ directory and create db models</h2>

```
cd src/ 
python manage.py migrate 
```

Run Server :

```runserver
python manage.py runserver
```

Now go to<a href="http://127.0.0.1:8000/"><ul><li> http://127.0.0.1:8000/</li></ul> </a>


<h2>ScreenShots</h2>
<ol>
  <li>Home Page : </li><br>
<img src="https://github.com/sohanur-it/E-Comerce-App/blob/master/screenshots/hom1.png"><br><br>

   <li>Product with Category Based : </li><br>
<img src="https://github.com/sohanur-it/E-Comerce-App/blob/master/screenshots/home2.png"><br><br>
  
 <li>Product with Detail Page: </li><br>
<img src="https://github.com/sohanur-it/E-Comerce-App/blob/master/screenshots/home3.png"><br><br>

 <li>Order Summary Page: </li><br>
<img src="https://github.com/sohanur-it/E-Comerce-App/blob/master/screenshots/home4.png"><br><br>

 <li>CheckOut Page: </li><br>
<img src="https://github.com/sohanur-it/E-Comerce-App/blob/master/screenshots/home5.png"><br><br>

 <li>Billing and Shipping Address: </li><br>
<img src="https://github.com/sohanur-it/E-Comerce-App/blob/master/screenshots/home6.png"><br><br>

   <li>Payment Page </li><br>
<img src="https://github.com/sohanur-it/E-Comerce-App/blob/master/screenshots/home7.png"><br><br>

  <li>Stripe Dashboard </li><br>
<img src="https://github.com/sohanur-it/E-Comerce-App/blob/master/screenshots/home8.png"><br><br>

 <li>Customized Admin Panel </li><br>
<img src="https://github.com/sohanur-it/E-Comerce-App/blob/master/screenshots/home9.png"><br><br>

 <li>Profile Page </li><br>
<img src="https://github.com/sohanur-it/E-Comerce-App/blob/master/screenshots/profile.png"><br><br>
  
</ol>


