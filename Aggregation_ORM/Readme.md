
# Target database is Music_shop
## Imports in python shell:
```from product.models import Trak
from payment.models import InvoiceLine
from user.models import Customer
from django.db.models import * (Avg, Max, Min, Count, FloatField,...)
from django.contrib.postgres.aggregates import ArrayAgg
```

## Queries:
###1) average on price field of tracks:
###### Django_ORM:
``
