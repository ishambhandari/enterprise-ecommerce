var user = "{{request.user}}";

const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
let updateBtns = document.getElementsByClassName("update-cart");
for (i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    console.log("this:", this);
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("productId:", productId, "Action:", action);
    console.log("USER", user);
    if (user === "AnonymousUser") {
      console.log("NOT LOGGED IN");
    } else {
      updateOrder(productId, action);
    }
  });
  function updateOrder(productId, action) {
    var url = "update-cart/";
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({ productId: productId, action: action }),
    })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        console.log("data", data);
      });
  }
}
