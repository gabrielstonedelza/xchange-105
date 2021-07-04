

audioPlayer();


function audioPlayer() {
    var currentSong = 0;
    
    $("#audioPlayer")[0].src = $("#playlist a")[0];
    $("#playlist a").on('click', function (event) {
        event.preventDefault();

        var tname = event.currentTarget.title;

        $("#audioPlayer")[0].src = this;
        $("#audioPlayer")[0].play();
        $(".nowplaying").html('<small class="playing">Now playing</small> ' + " " + tname)
    });
    $("#audioPlayer")[0].addEventListener("ended", function (event) {
        currentSong++;
        if (currentSong == $("#playlist a").length)
            currentSong = 0;
        $("#audioPlayer")[0].src = $("#playlist a")[currentSong].href;
        var name = $("#playlist a")[currentSong].title
        $("#audioPlayer")[0].play();

        $(".nowplaying").html('<small class="playing">Now playing</small> ' + " " + name)


    });
    $("#forward").on('click', function (event) {
        currentSong++;
        if (currentSong > $("#playlist a").length)
            currentSong = 0;
        $("#audioPlayer")[0].src = $("#playlist a")[currentSong].href;
        var name = $("#playlist a ")[currentSong].title
        $("#audioPlayer")[0].play();

        $(".nowplaying").html('<small class="playing">Now playing</small> ' + " " + name)

    })
    $("#back").on('click', function (event) {
        currentSong--;
        if (currentSong < 0)
            currentSong = 0;
        $("#audioPlayer")[0].src = $("#playlist a")[currentSong].href;
        var name = $("#playlist a ")[currentSong].title
        $("#audioPlayer")[0].play();
        $(".nowplaying").html('<small class="playing">Now playing</small> ' + " " + name)
    })
}

