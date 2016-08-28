## yaoguang-python-client

```Python
$ pip3 install yaoguang-python-client
$ python3
>>> from yaoguang.lead import Leads
>>> leads = Leads('bj2-storm03')
>>> lead = leads.get('******7896')
>>> printf(lead.ls())  # inspect fields
>>> lead  # repr as pretty json
{
    "bj_user_recycle_order_accrual_90": 10.0,
    "contact_id": "******7896",
    "tm_ad_num_max_sum_180_category": "ershouzixingche",
    "tm_ad_num_max_sum_180_city": "571",
    "tm_ad_num_max_sum_180_top_category": "cheliang",
    "tm_ad_num_sum_180": 1,
    "tm_user_account_balance": 0.0,
    "tm_user_create_time": 1416758400,
    "tm_user_last_login_time": 1467289872,
    "tm_user_last_recharge_time": 1464969600,
    "tm_user_recharge_amount_sum_360": 10.0
}
>>> lead['company']['latest_ads']['ad_id_xxx'] # chain access
```

