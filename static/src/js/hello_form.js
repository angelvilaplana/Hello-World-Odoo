odoo.define('hello_world.form', function(require) {
    "use strict";

    console.log('Hello World Form');

    let Form = require('web.FormController');

    let FormAction = Form.include({
        _onButtonClicked: function (event) {
            console.log('Click')
            this._super(event);
        }
    });

    return FormAction;
});