```javascript
odoo.define('custom_pc_odoo_17_v6.pricing', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var _t = core._t;

    var PricingEngine = {
        getCompetitivePrice: function(productId) {
            return ajax.jsonRpc('/api/pricing/competitive', 'call', {
                product_id: productId
            });
        },

        getBundleOffers: function(productId) {
            return ajax.jsonRpc('/api/pricing/bundle_offers', 'call', {
                product_id: productId
            });
        },

        applyDiscounts: function(productId, discountCode) {
            return ajax.jsonRpc('/api/pricing/apply_discount', 'call', {
                product_id: productId,
                discount_code: discountCode
            });
        }
    };

    return PricingEngine;
});
```