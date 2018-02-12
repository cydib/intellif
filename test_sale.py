#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-04 15:41:37
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
import datetime

now = datetime.datetime.now()

a = now.strftime('%Y-%m-%d')

sale_data = {
    "currencyCode": "BU0080001",
    "currencyName": "人民币",
    "customerCode": "82145594",
    "customerName": "honey",
    "customerOrderDocNo": "abc",
    "deliveryMethodCode": "FOB",
    "deliveryMethodName": "FOB",
    "docNo": "",
    "extraAmount": "5",
    "inventoryCount": "",
    "orderAmount": "",
    "paymentCode": "652a5908-79b3-431c-b119-0baeca23fd2e",
    "recAgreementCode": "5306be1a-959e-484f-9bbe-f5b2f25ef1e0",
    "recordId": "",
    "remark": "订单备注abc",
    "taxRate": "0",
    "saleInventoryVos": [
        {
            "inventoryCode": "FNDE-6",#货品编码
            "inventoryId": "5a12362b0ec38352e31874f2",
            "inventoryName": "自制件-AIT",
            "inventorySpec": "WDL",
            "inventoryCategoryCode": "M_62699706",
            "inventoryTypeCode": "001",
            "attributeCode": 1,
            "attributeName": "",
            "quantity": 120,#订单数量
            "spareQuantity": 7,#备品数量
            "recordId": "",
            "remark": "行备注",
            "unitName": "个",
            "unitPrice": 1.78,
            "deliveryDate": a,#交期
            "bomId": "06710ec6-9671-421d-b784-7245293616e1",
            "amount": "",#合计
            "inventoryAttachments": [
            ],
            "attributeCodeDisabled": "true"
        }
    ],
    "saleOrderAttachments": [
    ],
    "customerDeclaration": "",
    "currencySymbol": "AUD",
    "paymentName": "现金",
    "recAgreementName": "月结30天"
}

# print(type(json.dumps(sale_data)))
