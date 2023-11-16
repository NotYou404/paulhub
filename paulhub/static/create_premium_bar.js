function createPremiumBar() {
  let premiumBar = document.getElementById("premiumBar");
  premiumBar.innerHTML = `
    <style>
      .premium-bar {
        height: 40px;
        width: 100%;
        margin: auto;
        padding-left: 30px;
        padding-right: 30px;
        position: fixed;
      }
      .float-right-child {
        float: right;
      }
      .close {
        color: rgb(88, 88, 88);
        /*float: right;*/
        font-size: 35px;
        font-weight: bold;
        /*padding-top: 5px;
        padding-right: 7px;*/
        align-self: auto;
        vertical-align: middle;
      }
      .close:hover,
      .close:focus {
        color: #000;
        text-decoration: none;
        cursor: pointer;
      }
    </style>
    <div class="parent premium-bar">
      <h3 class="child" style="font-weight: bold;">Buy PaulHub Premium</h3>
      <button style="background-color: rgb(76, 76, 76); border: 0px solid #000000; border-radius: 4px; float: right; width: 30px; height: 30px;">
        <span class="close">&times;</span>
      </button>
    </div>
  `
}