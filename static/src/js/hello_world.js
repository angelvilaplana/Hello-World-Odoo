odoo.define('hello_world.main', function(require) {
    "use strict";

    console.log('Hello World!')

    let Attendance = require('hr_attendance.my_attendances');

    let HelloAction = Attendance.include({
        events: _.extend({}, _.result(Attendance.prototype, 'events') || {}, {
                "click .fa-sign-in": function () {
                    console.log('IN');
                },
                "click .fa-sign-out": function () {
                    console.log('OUT');
                }
            }
        )
    });
    
    return HelloAction;
});