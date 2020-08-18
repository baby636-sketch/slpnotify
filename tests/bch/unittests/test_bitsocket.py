import pytest
import requests_mock
from tests.bch.objects import obj_bitsocket
from tests.system.objects import obj_save_record

@pytest.mark.django_db
def test_bitsocket_transaction(requests_mock, capsys):
    source = 'bitsocket'
    # Test BitDBQuery from tasks.py
    script = obj_bitsocket.BitSocketTest(requests_mock, capsys)
    script.test()

    # Test recording of Transaction
    outputs = getattr(script, 'output', None).split("\n")
    assert(outputs)
    for output in outputs:
        args = [x.replace("'","").replace(")","").replace("(","").replace("None", "").strip() for x in output.split(',')]
        if len(output):
            saving = obj_save_record.SaveRecordTest()
            saving.test(*args)
            assert saving.address == args[1]
            assert saving.txid == args[2]
            assert saving.amount == args[3]
            assert saving.source == args[4] == source
            assert saving.spent_index == args[6]
            if args[5] != '':
                assert saving.blockheight == args[5]