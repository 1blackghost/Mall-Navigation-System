$(window).on('load', function() {
  // JavaScript to handle the hamburger menu toggle
const hamburgerBtn = document.querySelector('.hamburger-btn');
const menu = document.querySelector('.menu');

hamburgerBtn.addEventListener('click', function () {
  menu.classList.toggle('open');
});

  $(".map").hide();
  $('.tab-button, .floor-image').hide();

  var previewData = {
    start: [
        "Mall Office",
        "Data Center",
        "Stairs",
        "Floor 1 RestRoom",
        "Entrance Hall",
        "Service Counter",
        "Rest Area",
        "Elevator",
        "HP",
        "Apple",
        "Dell",
        "Samsung",
        "MyG",
        "Acer",
        "Hug A Mug",
        "KFC",
        "Dominos",
        "StarBucks",
        "Chicking",
        "McDonalds",
        "Chickos",
        "Stairs Floor 2",
        "RestArea Floor 2",
        "Mall Office Floor 2",
        "Gucci",
        "Rollex",
        "Rado",
        "Oris",
        "Titan",
        "Fastrack",
        "MI",
        "Floor 2 RestRoom",
        "Sony",
        "VGuard",
        "Panasonic",
        "Puma",
        "Louis Phillipie",
        "Addidas",
        "Trends",
        "Jockey",
        "Bata",
        "US POLO",
        "Stairs Floor 3",

    ],  

    destination: [
        "Mall Office",
        "Data Center",
        "Stairs",
        "Floor 1 RestRoom",
        "Entrance Hall",
        "Service Counter",
        "Rest Area",
        "Elevator",
        "HP",
        "Apple",
        "Dell",
        "Samsung",
        "MyG",
        "Acer",
        "Hug A Mug",
        "KFC",
        "Dominos",
        "StarBucks",
        "Chicking",
        "McDonalds",
        "Chickos",
        "Stairs Floor 2",
        "RestArea Floor 2",
        "Mall Office Floor 2",
        "Gucci",
        "Rollex",
        "Rado",
        "Oris",
        "Titan",
        "Fastrack",
        "MI",
        "Floor 2 RestRoom",
        "Sony",
        "VGuard",
        "Panasonic",
        "Puma",
        "Louis Phillipie",
        "Addidas",
        "Trends",
        "Jockey",
        "Bata",
        "US POLO",
        "Stairs Floor 3",

    ],  

  };

  function showPreviewResults() {
    var startInput = $('#start');
    var destinationInput = $('#destination');
    var previewSection = $('#preview');
    var previewList = $('#preview-list');

    var activeInput = document.activeElement;
    var activeInputId = activeInput.id;

    var inputValue = activeInput.value.trim();

    if (inputValue.length > 0) {
      var results = previewData[activeInputId].filter(function(result) {
        return result.toLowerCase().includes(inputValue.toLowerCase());
      });

      var previewContent = '';

      if (results.length > 0) {
        results.forEach(function(result) {
          previewContent += '<li>' + result + '</li>';
        });
      } else {
        previewContent += '<li>No results found</li>';
      }

      previewList.html(previewContent);
      previewSection.css('display', 'block');

      var previewItems = previewList.find('li');
      previewItems.each(function() {
        $(this).on('click', function() {
          if ($(this).text() !== 'No results found') {
            activeInput.value = $(this).text();
            previewSection.css('display', 'none');
          }
        });
      });
    } else {
      previewList.html('');
      previewSection.css('display', 'none');
    }
  }

  $('#submitBtn').on('click', function() {
    var startLocation = $('#start').val();
    var destinationLocation = $('#destination').val();

    // AJAX POST request
    $.ajax({
      type: 'POST',
      url: '/getPath',
      data: {
        start: startLocation,
        destination: destinationLocation
      },
      success: function(response) {
        if (response.status === 'ok') {
            var button = document.getElementById("toggleButton");
            button.checked = false;
          $(".map").show();
          var floors = response;
          delete floors.status; // Remove the 'status' property from the response object
          var time = response.time;
          $(".time-taken").text("Average Time:"+time+" minutes.")

          // Hide all floor buttons and images
          $('.tab-button, .floor-image').hide();
              var similarData = response.similar;
              var similarList = '';

              for (var i = 0; i < similarData.length; i++) {
                similarList += '<li>' + similarData[i][1] + '</li>';
              }

              $('#similar ul').html(similarList);
              $('#similar').show();
          for (var floor in floors) {
            if (floors.hasOwnProperty(floor)) {
              var floorData = floors[floor];
              var imgSrc = floorData.img;
              var floorNumber = floorData.floor;
              var currentImgSrc = $('#floor' + floorNumber).attr('src');

              // Check if the image source has changed
              if (currentImgSrc !== imgSrc) {
                // Show the corresponding floor button and image
                $('#floor' + floorNumber).attr('src', imgSrc);
                $('#floor' + floorNumber + 'Button').show();
                $('#floor' + floorNumber).show();
                $("#floor1Button").click();
                $("#floor2Button").click();
                $("#floor3Button").click();
                $("#floor"+floorNumber+"Button").click();

              }
            }
          }
        } else {
          console.log('Invalid response');
        }
      },
      error: function(xhr, status, error) {
        console.log('Error:', error);
      }
    });
  });

  $('#start').on('input', showPreviewResults);
  $('#destination').on('input', showPreviewResults);

  // Set initial active floor
  var activeFloor = 'floor1';

  // Function to switch active floor
  function switchFloor(floor) {
    // Remove active class from current floor button
    $('#' + activeFloor + 'Button').removeClass('active');

    // Hide current floor image
    $('#' + activeFloor).hide();

    // Add active class to new floor button
    $('#' + floor + 'Button').addClass('active');

    // Show new floor image
    $('#' + floor).show();

    // Update active floor variable
    activeFloor = floor;
  }

  // Floor button click event
  $('.tab-button').click(function() {
    var floor = $(this).attr('id').replace('Button', '');
    switchFloor(floor);
  });

  // Previous floor button click event
  $('#prevFloorButton').click(function() {
    var floorIndex = parseInt(activeFloor.replace('floor', ''));
    var prevFloor = 'floor' + (floorIndex - 1);
    if ($('#' + prevFloor).length > 0) {
      switchFloor(prevFloor);
    }
  });

  // Next floor button click event
  $('#nextFloorButton').click(function() {
    var floorIndex = parseInt(activeFloor.replace('floor', ''));
    var nextFloor = 'floor' + (floorIndex + 1);
    if ($('#' + nextFloor).length > 0) {
      switchFloor(nextFloor);
    }
  });
});
function toggleFloors() {
  var button = document.getElementById("toggleButton");
  if (button.checked) {
    $(".tab-button").show();
    $(".map").show();
    $("#floor1Button").click();
  } else {
    $(".tab-button").hide();
    $(".floor-image").hide();
    $(".map").hide();
  }
}
