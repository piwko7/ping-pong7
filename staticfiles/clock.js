function showTime(){
    var date = new Date();
    var h = date.getHours(); // 0 - 23
    var m = date.getMinutes(); // 0 - 59
    var s = date.getSeconds(); // 0 - 59

  
    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;   
    var time = h + ":" + m + ":" + s;


    var day = date.getDay();
    var weekday = new Array(7);
    weekday[0] = "Niedziela";
    weekday[1] = "Poniedziałek";
    weekday[2] = "Wtorek";
    weekday[3] = "Środa";
    weekday[4] = "Czwartek";
    weekday[5] = "Piątek";
    weekday[6] = "Sobota";
    var day = weekday[date.getDay()];


    var day_num = date.getDate();
    var month = date.getMonth();
    var year = date.getFullYear();
    var month_array = new Array(12);
    month_array[0] = "01";
    month_array[1] = "02";
    month_array[2] = "03";
    month_array[3] = "04";
    month_array[4] = "05";
    month_array[5] = "06";
    month_array[6] = "07";
    month_array[7] = "08";
    month_array[8] = "09";
    month_array[9] = "10";
    month_array[10] = "11";
    month_array[11] = "12";
    var month_day = month_array[month];
    var full_date = day_num + "/" + month_day + "/" + year;


    

    document.getElementById("DayDisplay").innerText = day;
    document.getElementById("DayDisplay").textContent = day;

    document.getElementById("MyClockDisplay").innerText = time;
    document.getElementById("MyClockDisplay").textContent = time;

    document.getElementById("DateDisplay").innerText = full_date;
    document.getElementById("DateDisplay").textContent = full_date;



    setTimeout(showTime, 1000);

}

showTime();