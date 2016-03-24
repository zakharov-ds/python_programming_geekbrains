var n = +prompt('введите количество строк',5);
    m = +prompt('введите количество столбцов',5);
if (n != NaN && m != NaN && n != 0 && m != 0) { // почему данное условие не срабатывает когда в n и m вводишь буквы? 
    console.log(m);
    console.log(n);
    document.addEventListener('DOMContentLoaded',function createTable()
    {
        var table = document.createElement("table");
            table.setAttribute('border','1');
            table.setAttribute('width','500');
            tr = "";
            td = "";
            text = "";
        for (var i = 0; i < n; i++) 
        {
          tr = document.createElement("tr");
          for (var j = 0; j < m; j++) 
          {
            td = document.createElement("td");
            text = document.createTextNode((i + 1) + "." + (j + 1));
            td.appendChild(text);
            tr.appendChild(td);
          }
          table.appendChild(tr);
        }
        console.log(tr);
        console.log(td);
        console.log(table);
        return document.body.appendChild(table);
    });
    } else {
        alert('В поле для кол-ва строк или столбцов введены не цифры!!!');
    };
//document.getElementsByTagName("body").appendChild(createTable());


