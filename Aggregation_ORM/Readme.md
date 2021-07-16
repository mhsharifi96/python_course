
# Target database is Music_shop
## Imports in python shell:
```
from product.models import Trak
from payment.models import InvoiceLine
from user.models import Customer
from django.db.models import *
from django.contrib.postgres.aggregates import ArrayAgg
```

## Queries:
### 1. average on price field of tracks:
###### Django_ORM:
```Track.objects.all().aggregate(Avg('unit_price'))```
###### Sql:
```
SELECT  AVG(unit_price) AS AVG_PRC
FROM public.product_track;
```

### 2. Difference between the highest priced track and the average price of all tracks:
###### Django_ORM:
```
Track.objects.aggregate(price_diff=Max('unit_price', output_field=FloatField()) - Avg('unit_price'))
```
###### Sql:
```
SELECT RSLT.MAXP - RSLT.AVP
FROM
(
SELECT MAX(unit_price) AS MAXP, AVG(unit_price) AS AVP
FROM public.product_track) AS RSLT;
```

### 3. average, maximum and minimum price of all tracks (more than one aggregate at the same time):
###### Django_ORM:
```
Track.objects.aggregate(Avg('unit_price'), Max('unit_price'), Min('unit_price'))
```
###### Sql:
```
SELECT MAX(unit_price), MIN(unit_price), AVG(unit_price)
FROM public.product_track;
```
 
### 4. chipest and most expensive price of sold tracks:
###### Django_ORM:
```
InvoiceLine.objects.aggregate(chipest=Min('track__unit_price'), most_expensive=Max('track__unit_price'))
```
###### Sql:
```
SELECT MIN(public.product_track.unit_price) AS CHIPEST, MAX(public.product_track.unit_price)AS M_EXP
FROM public.payment_invoiceline
JOIN public.product_track ON public.product_track.id=public.payment_invoiceline.track_id;
```
  
### 5. aggregation on query-set, average of price for tracks which their name starts with d:
###### Django_ORM:
```
Track.objects.filter(name__istartswith="D").aggregate(Avg('unit_price'))
```
###### Sql:
```
SELECT AVG(unit_price)
FROM public.product_track
WHERE public.product_track.name ~ '^[D].*';
```
   
### 6. list of prices for tracks chiper thas 1 dollor (not a practical example):
###### Django_ORM:
```
Track.objects.filter(unit_price__gt=1).aggregate(prices=ArrayAgg('unit_price'))
```
###### Sql:
```
SELECT ARRAY_AGG(unit_price)
FROM public.product_track
WHERE unit_price > 1;
```

### 7. list of fullname of customers who's name starts with d:
```
Customer.objects.filter(first_name__istartswith="D").aggregate(full=ArrayAgg(Concat('first_name', Value(' ') ,'last_name')
```
###### Sql:
```
SELECT ARRAY_AGG(first_name || ' ' || last_name)
FROM public.user_customer
WHERE first_name ~ '^[D].*';
```
_______________________________________________________

||: String concatenation

~: Matches regular expression, case sensitive

_______________________________________________________
# Usefull links:
[Django aggregate](https://docs.djangoproject.com/en/3.2/topics/db/aggregation/)

[PostgreSQL specific aggregation functions](https://docs.djangoproject.com/en/3.2/ref/contrib/postgres/aggregates/)

[Writing readme in github](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

