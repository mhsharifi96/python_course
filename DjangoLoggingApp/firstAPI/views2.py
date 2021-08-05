from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import logging,traceback
# logger = logging.getLogger(__name__)
logger = logging.getLogger("django")

def addUser(request):
    val={'response':'User Added'}
    print ('Hello adduser')
    logger.info('>>>>>>>>>>>>>> Something Debug wrong!')
    return JsonResponse(val,status=200)


def addSomething(request):
    val={'response':'Something Added'}
    logger.warning('Something warning wrong!')
    return JsonResponse(val,status=200)

def addNew(request,someNumber):
    val={'response':'Something Added New','numberGiven':int(someNumber)}
    if int(someNumber) > 50:
        return JsonResponse(val,status=500)
    else:
        logger.info('Something info2 wrong!')
        return JsonResponse(val,status=200)

def addNewError(request,someNumber):
    val={'response':'Something Added New','numberGiven':someNumber}
    try:
            
        if someNumber > 50:
            logger.error('Something error wrong!')
            return JsonResponse(val,status=500)
        else:
            logger.info('Something info wrong!')
            return JsonResponse(val,status=200)
    except Exception as e:
        print (str(e),traceback.format_exc())
