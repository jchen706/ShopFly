from django.shortcuts import render

from django.http import HttpResponse
from authorizenet import apicontractsv1

from authorizenet.apicontrollers import*

from decimal import*

from . form import CreditCardForm
merchantAuth = apicontractsv1.merchantAuthenticationType()

merchantAuth.name = "7URb6NF2uN"

merchantAuth.transactionKey = "9rWQN5p3T2Fyy85H"

def creditCardPayment(request):
    creditCard = apicontractsv1.creditCardType()
    form = CreditCardForm()

    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            try:
                creditCard_num = form.cleaned_data['creditCard_num']
            except (ValidationError):
                return render( request, 'new/card.html',{
                'error_message': "Invalid Card",
                })

            try:
                expirationDate = form.cleaned_data['expirationDate']
                amount = form.cleaned_data['amount']
                creditCard.cardNumber = str(creditCard_num)
                creditCard.expirationDate = str(expirationDate)
                payment = apicontractsv1.paymentType()
                payment.creditCard = creditCard

                transactionrequest = apicontractsv1.transactionRequestType()
                transactionrequest.transactionType ="authCaptureTransaction"
                transactionrequest.amount = amount

                transactionrequest.payment = payment

                #code from api
                createtransactionrequestapicontractsv1.createTransactionRequest()
                createtransactionrequest.merchantAuthentication = merchantAuth
                createtransactionrequest.refId ="MerchantID01"



                createtransactionrequest.transactionRequest = transactionrequest
                createtransactioncontroller=createTransactionController(createtransactionrequest)
                createtransactioncontroller.execute()

                response = createtransactioncontroller.getresponse()

                if (response.messages.resultCode=="Ok"):
                       message = "Transaction ID : %s"% response.transactionResponse.transId
                else:
                       message ="response code: %s"% response.messages.resultCode



                return render (request , 'new/card.html', {"message": message},)
            except (ValidationError):
                return render( request, 'new/card.html',{
                'error_message': "Card Expired!",
                })
    return render( request, 'new/card.html',)
