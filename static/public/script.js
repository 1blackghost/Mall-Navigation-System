$(window).on('load', function() {
  var previewData = {
    start: [
      'Start Preview 1',
      'Start Preview 2',
      'Start Preview 3'
    ],
    destination: [
      'Destination Preview 1',
      'Destination Preview 2',
      'Destination Preview 3'
    ]
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
        var floors = response;
        delete floors.status; // Remove the 'status' property from the response object

        for (var floor in floors) {
          if (floors.hasOwnProperty(floor)) {
            var floorData = floors[floor];
            var imgSrc = floorData.img;
            var floorNumber = floorData.floor;
            $('#floor' + floorNumber).attr('src', imgSrc);
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
});
