```javascript
odoo.define('custom_pc_odoo_17_v6.pc_builder', function (require) {
    "use strict";

    var core = require('web.core');
    var Widget = require('web.Widget');
    var rpc = require('web.rpc');

    var PcBuilderWidget = Widget.extend({
        template: 'PcBuilder',
        events: {
            'click .component-slot': '_onComponentSlotClick',
            'click .add-to-cart': '_onAddToCartClick',
        },

        init: function (parent, options) {
            this._super(parent, options);
            this.components = [];
            this.selectedComponents = {};
        },

        start: function () {
            var self = this;
            return this._fetchComponents().then(function (components) {
                self.components = components;
                self._renderComponents();
            });
        },

        _fetchComponents: function () {
            return rpc.query({
                model: 'product.product',
                method: 'search_read',
                domain: [['is_component', '=', true]],
                fields: ['name', 'image', 'price', 'specifications'],
            });
        },

        _renderComponents: function () {
            var self = this;
            _.each(this.components, function (component) {
                var $component = $(core.qweb.render('ComponentSlot', {component: component}));
                $component.appendTo(self.$('.components'));
            });
        },

        _onComponentSlotClick: function (event) {
            var componentId = $(event.currentTarget).data('id');
            var component = _.findWhere(this.components, {id: componentId});
            this.selectedComponents[component.type] = component;
            this._updatePrice();
        },

        _onAddToCartClick: function () {
            rpc.query({
                model: 'sale.order',
                method: 'create_from_components',
                args: [this.selectedComponents],
            }).then(function (orderId) {
                window.location.href = '/shop/cart';
            });
        },

        _updatePrice: function () {
            var total = _.reduce(this.selectedComponents, function (sum, component) {
                return sum + component.price;
            }, 0);
            this.$('.total-price').text(total.toFixed(2));
        },
    });

    core.action_registry.add('pc_builder', PcBuilderWidget);

    return PcBuilderWidget;
});
```