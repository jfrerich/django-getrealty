$(document).ready(function() {
    var dt_table = $('.datatable').dataTable({
        dom: "flrtip",
        language: dt_language,  // global variable defined in html
        order: [[ 0, "desc" ]],
        lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
        columnDefs: [
            {orderable: true,
             searchable: true,
             className: "center",
             targets: [0, 1]
            },
            {
                name: 'r_num',
                targets: [0]
            },
            {
                name: 'Property_Interest',
                targets: [1]
            }
        ],
        'rowCallback': function(row, data, index){

          // $("thead ").css("border-right: 1px solid #ddd");
          // $(row).css('background-color', '#B8B8B8');
          // window.alert('jason - TEST row=' + row + 'data=' + data.rpg)

          // r_num
          if(/^M/.test(data.r_num)){ 
              $('td:eq(0)',row).css('background-color', '#BFECC7');
          } else {
              $('td:eq(0)',row).css('background-color', '#B8B8B8');
          }

          // Property Interest
          if(/Not Vetted/.test(data[1])) { 
              $('td:eq(1)',row).css('background-color', '#FFF381');
          } else if(/Vetting/.test(data.Property_Interest)) { 
              $('td:eq(1)',row).css('background-color', '#FF8EC5');
          } else if(/Vetted - Other/.test(data.Property_Interest)) { 
              $('td:eq(1)',row).css('background-color', '#FF5B01');
          } else if(/Vetted - No Good/.test(data.Property_Interest)) { 
              $('td:eq(1)',row).css('background-color', '#D80608');
          } else if(/Vetted - Need to Call/.test(data.Property_Interest)) { 
              $('td:eq(1)',row).css('background-color', '#8FC502');
          } else if(/Owner Called - No contact/.test(data.Property_Interest)) { 
              $('td:eq(1)',row).css('background-color', '#FF8E02');
          } else if(/Owner Called - Low Interest/.test(data.Property_Interest)) { 
              $('td:eq(1)',row).css('background-color', '#015912');
          } else if(/Owner Called - High Interest/.test(data.Property_Interest)) { 
              $('td:eq(1)',row).css('background-color', '#1DAE15');
          } else if(/Owner Called - Will not sell/.test(data.Property_Interest)) { 
              $('td:eq(1)',row).css('background-color', '#FE9D3E');
          } else if(/Owner Called - Negotiating/.test(data.Property_Interest)) { 
              $('td:eq(1)',row).css('background-color', '#8EC5FF');
          } else if(/Prop - Sold/.test(data.Property_Interest)) { 
              $('td:eq(1)',row).css('background-color', '#FFC502');
          } else if(/Prop - Bought/.test(data.Property_Interest)) { 
              $('td:eq(1)',row).css('background-color', '#45DE4D');
          }

          if(data.Maps___map== 'n/a'){ // map
              $(row).find('td:eq(7)').css('background-color', '#FFC502');
          }

          if(data.Tax_Due___PctToAss < 5){ 
              $('td:eq(13)',row).css('background-color', '#BFECC7');
          } else if(data.Tax_Due___PctToAss >= 5 && data.Tax_Due___PctToAss <= 20) { 
              $('td:eq(13)',row).css('background-color', '#FFC502');
          } else if(data.Tax_Due___PctToAss > 20){ 
              $('td:eq(13)',row).css('background-color', '#FF8EC5');
          }

          if(/^0/.test(data.Different___Addr)) { 
              $('td:eq(19)',row).css('background-color', '#FF8EC5');
          } else if(/^1/.test(data.Different___Addr)) { 
              $('td:eq(19)',row).css('background-color', '#BFECC7');
          } else if(data.Different___Addr == 'n/a') { 
              $('td:eq(19)',row).css('background-color', '#FFC502');
          }

          if(data.Different___Zip == 0) { 
              $('td:eq(20)',row).css('background-color', '#FF8EC5');
          } else if(data.Different___Zip == 1) { 
              $('td:eq(20)',row).css('background-color', '#BFECC7');
          } else if(data.Different___Zip == 'n/a') { 
              $('td:eq(20)',row).css('background-color', '#FFC502');
          }

          if(data.Different___State == 0) { 
              $('td:eq(21)',row).css('background-color', '#FF8EC5');
          } else if(/1 - \S\S/.test(data.Different___State)) { 
              $('td:eq(21)',row).css('background-color', '#BFECC7');
          } else if(data.Different___State == 'n/a') { 
              $('td:eq(21)',row).css('background-color', '#FFC502');
          }

          if(data.NHS_imp == 1) { 
              $('td:eq(22)',row).css('background-color', '#BFECC7');
          } else if(data.NHS_imp == 0) { 
              $('td:eq(22)',row).css('background-color', '#FF8EC5');
          }
          $('td:eq(26)',row).css('background-color', '#B8B8B8'); // Appraised___AppPctOfMax
          $('td:eq(31)',row).css('background-color', '#B8B8B8'); // Assessed___AssPctOfMax
          $('td:eq(36)',row).css('background-color', '#B8B8B8'); // ImpNHS___LastPctOfMax
          $('td:eq(41)',row).css('background-color', '#B8B8B8'); // IMPHS___ihsAppPctOfMax
          $('td:eq(46)',row).css('background-color', '#B8B8B8'); // LandHS___lhsAppPctOfMax
          $('td:eq(51)',row).css('background-color', '#B8B8B8'); // LandNHS___lnhsAppPctOfMax

          if(/^1/.test(data.PctDiffAddr)) { 
              $('td:eq(58)',row).css('background-color', '#FBECC7');
          } else if(/^0/.test(data.PctDiffAddr)) { 
              $('td:eq(58)',row).css('background-color', '#FF8EC5');
          } else if(data.PctDiffAddr == 'n/a') { 
              $('td:eq(58)',row).css('background-color', '#FFC502');
          }

		    },
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        ajax: TESTMODEL_LIST_JSON_URL
    });
});
