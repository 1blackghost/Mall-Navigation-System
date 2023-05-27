$(window).on('load', function() {
    const hamburgerBtn = document.querySelector('.hamburger-btn');
    const menu = document.querySelector('.menu');

    hamburgerBtn.addEventListener('click', function() {
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

        $.ajax({
            type: 'POST',
            url: '/getPath',
            data: {
                start: startLocation,
                destination: destinationLocation
            },
            success: function(response) {
                if (response.status === 'ok') {
                    $(".time-taken").show();
                    var button = document.getElementById("toggleButton");
                    button.checked = false;
                    $(".map").show();
                    var floors = response;
                    delete floors.status;
                    var time = response.time;
                    $(".time-taken").text("Average Time:" + time + " minutes.")

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

                            if (currentImgSrc !== imgSrc) {
                                $('#floor' + floorNumber).attr('src', imgSrc);
                                $('#floor' + floorNumber + 'Button').show();
                                $('#floor' + floorNumber).show();
                                $("#floor1Button").click();
                                $("#floor2Button").click();
                                $("#floor3Button").click();
                                $("#floor" + floorNumber + "Button").click();

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

    var activeFloor = 'floor1';

    function switchFloor(floor) {
        $('#' + activeFloor + 'Button').removeClass('active');

        $('#' + activeFloor).hide();

        $('#' + floor + 'Button').addClass('active');

        $('#' + floor).show();

        activeFloor = floor;
    }

    $('.tab-button').click(function() {
        var floor = $(this).attr('id').replace('Button', '');
        switchFloor(floor);
    });

    $('#prevFloorButton').click(function() {
        var floorIndex = parseInt(activeFloor.replace('floor', ''));
        var prevFloor = 'floor' + (floorIndex - 1);
        if ($('#' + prevFloor).length > 0) {
            switchFloor(prevFloor);
        }
    });

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