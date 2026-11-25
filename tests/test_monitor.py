import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'bitcoin-node-monitor'))
from monitor import RPC, snapshot, configs

class Fake:
    def call(self,m):
        return {'getblockchaininfo':dict(blocks=5,headers=8,initialblockdownload=True,verificationprogress=.5,size_on_disk=2**30,chain='main',pruned=False), 'getnetworkinfo':dict(connections=0,connections_in=0,connections_out=0,subversion='/Satoshi:31.0/'), 'getnettotals':dict(totalbytesrecv=0,totalbytessent=0),'uptime':12}[m]

class Tests(unittest.TestCase):
    def test_snapshot(self):
        s,p=snapshot(Fake(),{},100,30)
        self.assertEqual(s['disk_gib'],1); self.assertTrue(s['no_peers']); self.assertFalse(s['synchronized']); self.assertIsNone(s['prune_height'])
    def test_stall(self):
        _,p=snapshot(Fake(),{},100,30)
        s,_=snapshot(Fake(),p,1900,30); self.assertTrue(s['sync_stalled'])
    def test_discovery(self):
        c=list(configs('test','homeassistant',180)); self.assertEqual(len(c),19); self.assertEqual(len({x[1]['unique_id'] for x in c}),19)
    def test_http_opt_in(self):
        with self.assertRaises(ValueError): RPC(dict(rpc_url='http://localhost:8332',allow_insecure_rpc=False))
    def test_whitelist(self):
        r=RPC(dict(rpc_url='https://localhost:8332',rpc_username='monitor',rpc_password='test',allow_insecure_rpc=False))
        with self.assertRaises(ValueError): r.call('stop')
    def test_url_credentials(self):
        with self.assertRaises(ValueError): RPC(dict(rpc_url='https://user:pass@localhost:8332'))

if __name__=='__main__': unittest.main()
