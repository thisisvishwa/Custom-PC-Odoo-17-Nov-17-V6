```javascript
odoo.define('custom_pc_odoo_17_v6.review', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var publicWidget = require('web.public.widget');

    var _t = core._t;

    publicWidget.registry.ReviewWidget = publicWidget.Widget.extend({
        selector: '#review-section',
        events: {
            'click .submit-review': '_onSubmitReview',
        },

        start: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                self._updateReviewSection();
            });
        },

        _updateReviewSection: function () {
            var self = this;
            ajax.jsonRpc("/shop/review", 'call', {}).then(function (data) {
                if (data) {
                    self.$('.review-list').html(data);
                }
            });
        },

        _onSubmitReview: function (ev) {
            ev.preventDefault();
            var self = this;
            var $form = $(ev.currentTarget).closest('form');
            var reviewData = $form.serializeArray().reduce(function (obj, item) {
                obj[item.name] = item.value;
                return obj;
            }, {});

            ajax.jsonRpc("/shop/review/submit", 'call', reviewData).then(function (data) {
                if (data.success) {
                    self._updateReviewSection();
                    alert(_t("Review submitted successfully!"));
                } else {
                    alert(_t("Failed to submit review. Please try again."));
                }
            });
        },
    });

    return publicWidget.registry.ReviewWidget;
});
```