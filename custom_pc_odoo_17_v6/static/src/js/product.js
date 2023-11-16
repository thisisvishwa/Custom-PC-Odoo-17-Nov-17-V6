```javascript
odoo.define('custom_pc_odoo_17_v6.product', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var publicWidget = require('web.public.widget');

    var QWeb = core.qweb;
    var _t = core._t;

    publicWidget.registry.ProductWidget = publicWidget.Widget.extend({
        selector: '#product-list',
        events: {
            'click .product-card': '_onProductCardClick',
        },

        start: function () {
            return $.when(
                ajax.loadXML("/custom_pc_odoo_17_v6/static/src/xml/product.xml", QWeb),
                this._super.apply(this, arguments)
            );
        },

        _onProductCardClick: function (event) {
            event.preventDefault();
            var $card = $(event.currentTarget);
            var productId = $card.data('product-id');
            this._getProductDetails(productId);
        },

        _getProductDetails: function (productId) {
            this._rpc({
                route: '/api/products/' + productId,
                params: { context: this.getSession().user_context },
            }).then(this._handleProductDetails.bind(this));
        },

        _handleProductDetails: function (product) {
            if (!product) {
                this.displayNotification({
                    title: _t('Error'),
                    message: _t('Product not found'),
                    type: 'danger',
                });
                return;
            }
            this._displayProductDetails(product);
        },

        _displayProductDetails: function (product) {
            var $content = $(QWeb.render('custom_pc_odoo_17_v6.ProductDetails', { product: product }));
            this.$el.html($content);
        },
    });

    return publicWidget.registry.ProductWidget;
});
```