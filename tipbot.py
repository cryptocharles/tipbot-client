import sys
import json
import click
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)
server_url = 'http://10.244.195.170:7777/tipbot/tips/'

@click.command()
@click.argument('username')
@click.argument('amount')
def cli(username, amount):
    sel_url = server_url+'{}?amount={}'.format(username, amount)
    click.echo(json.loads(requests.get(url=sel_url)))

@click.command()
def last():
    click.echo(json.loads(requests.get(url=server_url+'/last-tips')))
