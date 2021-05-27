var lightChart = document.getElementById("lightChart");
var dryChart = document.getElementById("dryChart");
var phChart = document.getElementById("phChart");
var relayCtrlChart = document.getElementById("relayCtrlChart");
var nodeConnection = document.getElementById("node1");
var relayCtrlSys = document.getElementById("relay-ctrl-sys");

var lightDataPoints = [],
	dryDataPoints = [],
	phDataPoints = [],
	relayCtrlDataPoints = [],
	currentDate = new Date(),
	currentLightValue = 0,
	currentDryValue = 0,
	currentPhValue = 0,
	relayCtrlStatus = "NA",
	lightMaxValue = 255,
	dryMaxValue = 255,
	phMaxValue = 255,
	nodeConnectedStatus = "home/node1 - NA",
	relayCtrlSystemStatus = "NA";

function load() {
	$.getJSON("/getjson", function (data) {
		data.data.forEach(element => {

			var dateStr = (currentDate.toLocaleDateString());
			dateSplit = dateStr.split("/")
			dateStr = dateStr.replace(dateSplit[0], "")
			dateStr = ("0" + dateSplit[0]).slice(-2) + dateStr
			
			if (dateStr == element.date) {	
				console.log(dateStr);
				lightDataPoints.push(element.data.light);
				dryDataPoints.push(element.data.dry);
				phDataPoints.push(element.data.ph);
				relayCtrlDataPoints.push(element.data.relay_ctrl.toUpperCase() == "ON" ? 1 : 0);
			}

			if (currentDate.getHours() == element.time) {
				currentLightValue = element.data.light;
				currentDryValue = element.data.dry;
				currentPhValue = element.data.ph;
				nodeConnectedStatus = element.data.node;
				relayCtrlSystemStatus = element.data.relay_ctrl;
			}
		});

		var myChart = new Chart(lightChart, {
			type: "line",
			data: {
				labels: ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"],
				datasets: [{
					label: "Sun Light (Max - 255)",
					fill: false,
					lineTension: 0.1,
					backgroundColor: "rgba(75,192,192,0.4)",
					borderColor: "rgba(255,150,0,1)",
					borderCapStyle: 'butt',
					borderDash: [],
					borderDashOffset: 0.0,
					borderJoinStyle: 'miter',
					pointBorderColor: "rgba(75,192,192,1)",
					pointBackgroundColor: "#fff",
					pointBorderWidth: 1,
					pointHoverRadius: 5,
					pointHoverBackgroundColor: "rgba(75,192,192,1)",
					pointHoverBorderColor: "rgba(220,220,220,1)",
					pointHoverBorderWidth: 2,
					pointRadius: 1,
					pointHitRadius: 5,
					data: lightDataPoints,
					spanGaps: false,
				}]
			},
			options: {
				scales: {
					yAxes: [{
						scaleLabel: {
							display: true,
							labelString: 'Light Level'
						}
					}],
					xAxes: [{
						scaleLabel: {
							display: true,
							labelString: 'Time'
						}
					}]
				}
			}
		});

		var myChart = new Chart(dryChart, {
			type: "line",
			data: {
				labels: ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"],
				datasets: [{
					label: "Water dry",
					fill: false,
					lineTension: 0.1,
					backgroundColor: "rgba(75,192,192,0.4)",
					borderColor: "rgba(75,192,192,1)",
					borderCapStyle: 'butt',
					borderDash: [],
					borderDashOffset: 0.0,
					borderJoinStyle: 'miter',
					pointBorderColor: "rgba(75,192,192,1)",
					pointBackgroundColor: "#fff",
					pointBorderWidth: 1,
					pointHoverRadius: 5,
					pointHoverBackgroundColor: "rgba(75,192,192,1)",
					pointHoverBorderColor: "rgba(220,220,220,1)",
					pointHoverBorderWidth: 2,
					pointRadius: 1,
					pointHitRadius: 5,
					data: dryDataPoints,
					spanGaps: false,
				}]
			},
			options: {
				scales: {
					yAxes: [{
						scaleLabel: {
							display: true,
							labelString: 'Water Level'
						}
					}],
					xAxes: [{
						scaleLabel: {
							display: true,
							labelString: 'Time'
						}
					}]
				}
			}
		});

		var myChart = new Chart(phChart, {
			type: "line",
			data: {
				labels: ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"],
				datasets: [{
					label: "PH",
					fill: false,
					lineTension: 0.1,
					backgroundColor: "rgba(75,192,192,0.4)",
					borderColor: "rgba(75,0,0,1)",
					borderCapStyle: 'butt',
					borderDash: [],
					borderDashOffset: 0.0,
					borderJoinStyle: 'miter',
					pointBorderColor: "rgba(75,192,192,1)",
					pointBackgroundColor: "#fff",
					pointBorderWidth: 1,
					pointHoverRadius: 5,
					pointHoverBackgroundColor: "rgba(75,192,192,1)",
					pointHoverBorderColor: "rgba(220,220,220,1)",
					pointHoverBorderWidth: 2,
					pointRadius: 1,
					pointHitRadius: 5,
					data: phDataPoints,
					spanGaps: false,
				}]
			},
			options: {
				scales: {
					yAxes: [{
						scaleLabel: {
							display: true,
							labelString: 'PH Level'
						}
					}],
					xAxes: [{
						scaleLabel: {
							display: true,
							labelString: 'Time'
						}
					}]
				}
			}
		});

		var myChart = new Chart(relayCtrlChart, {
			type: "line",
			data: {
				labels: ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"],
				datasets: [{
					label: "Relay Control System",
					fill: false,
					lineTension: 0.1,
					backgroundColor: "rgba(75,192,192,0.4)",
					borderColor: "rgba(75,0,0,1)",
					borderCapStyle: 'butt',
					borderDash: [],
					borderDashOffset: 0.0,
					borderJoinStyle: 'miter',
					pointBorderColor: "rgba(75,192,192,1)",
					pointBackgroundColor: "#fff",
					pointBorderWidth: 1,
					pointHoverRadius: 5,
					pointHoverBackgroundColor: "rgba(75,192,192,1)",
					pointHoverBorderColor: "rgba(220,220,220,1)",
					pointHoverBorderWidth: 2,
					pointRadius: 1,
					pointHitRadius: 5,
					data: relayCtrlDataPoints,
					spanGaps: false,
				}]
			},
			options: {
				scales: {
					yAxes: [{
						scaleLabel: {
							display: true,
							labelString: 'ON Status'
						}
					}],
					xAxes: [{
						scaleLabel: {
							display: true,
							labelString: 'Time'
						}
					}]
				}
			}
		});

		$('.light-current-value').knob({
			angleArc: 250,
			angleOffset: -125,
			readOnly: true,
			min: 0,
			max: lightMaxValue,
			fgColor: '#ffdd1f',
			height: 290,
			width: '95%'
		});

		$('.light-current-value').val(currentLightValue).trigger('change');

		// ----------------------------------------
		// Errors Detected
		// ----------------------------------------

		$('.dry-current-value').knob({
			angleArc: 250,
			angleOffset: -125,
			readOnly: true,
			min: 0,
			max: dryMaxValue,
			fgColor: '#00bbde',
			height: 290,
			width: '95%'
		});

		$('.dry-current-value').val(currentDryValue).trigger('change');

		$('.ph-current-value').knob({
			angleArc: 250,
			angleOffset: -125,
			readOnly: true,
			min: 0,
			max: phMaxValue,
			fgColor: '#fe6672',
			height: 290,
			width: '95%'
		});

		$('.ph-current-value').val(currentPhValue).trigger('change');


		nodeConnection.innerHTML = nodeConnectedStatus;
		if (nodeConnectedStatus == "Device Connected") {
			nodeConnection.style.backgroundColor = "#006400";
		} else {
			nodeConnection.style.backgroundColor = "red";
		}

		relayCtrlSys.innerHTML = relayCtrlSystemStatus;

		if(relayCtrlSystemStatus == "ON") {
			relayCtrlSys.style.backgroundColor = "#006400";
		} else {
			relayCtrlSys.style.backgroundColor = "red";
		}

		function timedRefresh(timeoutPeriod) {
			setTimeout("location.reload(true);",timeoutPeriod);
		}    
		
		window.onload = timedRefresh(100000); 
		// window.onload = timedRefresh(10000); 

	});
}
