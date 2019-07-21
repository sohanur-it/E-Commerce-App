<html>
<head>
<style>
  div{
  background-color:gray
}
  </style>
</head>
  <body>
# E-Comerce-App
<h4>
Create a superUser account before interacting with User, Account, Model and Admin Privilages
</h4>
<h2>
Main Features :
</h2>
<ul>
<li> Full Featured E-Commerce Application Product and Custom Post</li>
  <li> DetailView of Each Product With ADD/REMOVE Cart Facilities</li>
    <li> Custom Admin Panel </li>
  <li> Order Summary with total bill </li>
  <li> Checkout View with Product List </li>
    <li> Discount cupon Option for product </li>
    <li> Payment Option Stripe/Paypal </li>
  <li> Stripe Api Customization</li>
  <li>Category Based Product with price,title and image and others attributes </li>
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

<h4>
Linux -->
</h4>
<div style="background-color:gray">
virtualenv -p /usr/bin/python3 djecom <br>
cd djecom
</div>



<h4>
Windows -->
</h4>
<div>
virtualenv djecom <br>
cd .\djecom\
</div>


<h2>Activate virtualenv :</h2>
<h4>Linux -->
</h4>
<div>
source bin/activate
</div>


<h4>Windows--></h4>
<div>
.\Scripts\activate
</div>

<h2>
clone the project in the dj directory.
</h2>

<div>
git clone https://github.com/sohanur-it/E-Comerce-App.git
</div>

<div>
mv E-Comerce-App src/ <br>
cd src/  <br>
mv src/  <br>
mv requirements.txt ../ <br>
</div>

<h2>Install requirements.txt
</h2>
<div>
python -m pip install -r requirement.txt
</div>
<h2>
Now goto src/ directory and create db models.
</h2>


<div>
cd src/ <br>
python manage.py migrate <br>
</div>

<h2>Run Server :</h2>
<div>
python manage.py runserver
</div>
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
  
</ol>

</body>

</html>

