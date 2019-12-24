$(document).ready(function () {
    $(".cancel-button").click(function () {
        $.ajax({
            url: "/api/order/" + $(this).val() + "/",
            type: "DELETE",
            success: function (msg) {
                console.log(msg)
                if (msg.before_amount == 0 && msg.after_amount > 0) {
                    alert("商品到貨囉")
                };
                location.reload();
            }
        });
    });

    $(".purchase-button").click(function () {
        $.ajax({
            url: "/api/order/",
            type: "POST",
            data: {
                "product": $("#product_id").val(),
                "qy": $("#product_qy").val(),
                "customer": 1,
            },
            success: function (msg) {
                console.log(msg);
                alert("訂單已建立");
                location.reload();
            },
            error: function (error) {
                var parse_data = JSON.parse(error.responseText);
                alert(parse_data.detail.message);
            },
        });
    });

    $(".top3").click(function () {
        $.ajax({
            url: "/api/top_3/",
            type: "GET",
            success: function (msg) {
                console.log(msg);
                top3_list = []
                for (var i = 0; i < msg.length; i++) {
                    top3_list.push(JSON.stringify(msg[i]));
                }
                alert(top3_list);
            },
        });
    });
});
