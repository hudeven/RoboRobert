    function init() {
      var button_up = webiopi().createButton(
        "bt_up",
        "/\\",
        go_forward,
        stop);

      var button_down = webiopi().createButton(
        "bt_up",
        "\\/",
        go_back,
        stop);

      var button_left = webiopi().createButton(
        "bt_left",
        "<",
        turn_left,
        stop);

      var button_right = webiopi().createButton(
        "bt_right",
        ">",
        turn_right,
        stop);

      $("#box").append(button_up);
      $("#box").append(button_down);
      $("#box").append(button_left);
      $("#box").append(button_right);
      
    }
    
    function speed_up() {
       w().callMacro("speed_up");
       // var speed_label = document.getElementById("speed_label");
    }
 
    function speed_down() {
      w().callMacro("speed_down");
    }

    function go_forward() {
      w().callMacro("go_forward");
    }

    function go_back() {
      w().callMacro("go_back");
    }

    function turn_left() {
      w().callMacro("turn_left");
    }

    function turn_right() {
      w().callMacro("turn_right");
    }

    function stop() {
      w().callMacro("stop");
    }

    webiopi().ready(init);
 

