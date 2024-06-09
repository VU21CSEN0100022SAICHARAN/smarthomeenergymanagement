<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the input data
    $user_id = intval($_POST['user_id']);
    $appliance_id = intval($_POST['appliance_id']);
    $day_of_week = intval($_POST['day_of_week']);
    $hour = intval($_POST['hour']);

    // Command to run the Python script
    $command = escapeshellcmd("python C:\\xampp\\htdocs\\smart_home_energy_management\\machine_learning\\predict_energy_usage.py $user_id $appliance_id $day_of_week $hour");
    $output = shell_exec($command);

    // Return the prediction result
    echo json_encode(array("predicted_usage" => $output));
}
?>
