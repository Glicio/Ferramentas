let valorInput = document.getElementById("valor");
tabela = document.getElementById("tabela-memorandos");
valorInput.addEventListener('keydown', checkNumero);
valorInput.addEventListener('keyup', formatarNumero);

window.onload = function() {
  formatarTabela();
};

var formatter = new Intl.NumberFormat('pt-br', {
    style: 'currency',
    currency: 'BRL',

    // These options are needed to round to whole numbers if that's what you want.
    //minimumFractionDigits: 0, // (this suffices for whole numbers, but will print 2500.10 as $2,500.1)
    //maximumFractionDigits: 0, // (causes 2500.99 to be printed as $2,501)
  });
function formatarTabela(){
    for(let i = 1; i < tabela.rows.length; i++){
        valor_cell = tabela.rows[i].cells[4].innerText
        tabela.rows[i].cells[4].innerText = formatter.format(valor_cell)
    }
    for(let i = 1; i < tabela.rows.length; i+=2){
        tabela.rows[i].setAttribute("style", "background-color: #ddd;");
        console.log(tabela.rows[i])
    }
}
function checkNumero(e){
    //console.log(e.key == "Backspace");
    if(!/^([0-9])$/.test(e.key) && e.key != "Backspace" && e.key !="Tab" && e.key !="Enter"){
        e.preventDefault();
        return false;
    }
}

function formatarNumero(el){
    valor = el.target.value
    valor = valor.replace(".","")
    if(valor.length > 0){
        for(let i=0; i<valor.length; i++){

            if(valor.charAt(i) == "0" && valor.length > 4){
                valor = valor.substring(i+1,valor.length);
                break;
            }
            else{
                break;
            }
        }
        vl = valor.length
        if(vl < 4){
            valor = "0"+valor.substring(0, valor.length-2)+"."+valor.substring(valor.length-2,valor.length);
        }else{
            valor = valor.substring(0, valor.length-2)+"."+valor.substring(valor.length-2,valor.length);
        }
        el.target.value = valor;
    }
}