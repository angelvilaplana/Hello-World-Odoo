odoo.define('hello_world.report', function(require) {
    "use strict";

    console.log('Hello World Report');

    /*

    let ReportManager = require('web.ActionManager');
    console.log(ReportManager)

    let ReportActionManager = ReportManager.include({
        _triggerDownload: function (action, options, type) {
            console.log(action);
            console.log(options)
            console.log(type);
        }
    });

    return ReportActionManager;
    */
});