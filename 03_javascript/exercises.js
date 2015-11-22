
        //fucntion
      /*  var someText = 'This is my text';
        var splitted =someText.split(' ');
        document.write("lets check" + splitted[0]);
        document.write("lets check" + splitted.length);*/

      //  var text = 'hello my foot';
        //var keywords = text.split(' ');

    function keywordusage(text, keywords)
        {
              var f;
              var g=0;
              var answer = [];
              var splitted = text.split(' ');
              for (var j = 0; j < (keywords.length); j++)
              {
                    g=0;
                    for (var i = 0;i< splitted.length; i++)
                    {
                       if(splitted[i] === keywords[j] && j === 0)
                            {
                              answer.push(true);
                              g =1;
                            }
                          if (g===0 && i === (splitted.length)-1)
                            {
                              answer.push(false);
                            }


                    }
              }
            return answer;
        }

          function frequencies(text , wordlist)
          {
              var f;
              var answer={};
            //  answer["name"]++;
              var splitted = text.split(' ');
                for (var j = 0; j < wordlist.length; j++)
                {
                      answer[wordlist[j]]=0;
                      for (var i = 0;i< splitted.length; i++)
                        {
                          if(splitted[i] === wordlist[j])
                            {
                                answer[wordlist[j]] ++   ;
                            }

                        }
                }

                return answer;
          }


          function rotate(arra , steps)
          {
            var popped;

              if (steps === undefined)
                {
                  steps=1;
                }

              if(steps<0)
              {
                for(var i=0 ;i> steps ;i--)
                {
                    popped = arra.shift();
                    arra.push(popped);
                    console.log(i, arra);
                  }
                }
                else
                {
                  for(var i=0 ;i < steps ;i++)
                  {
                      shifted = arra.pop();
                      arra.unshift(shifted);
                  }
                }
            return arra ;
          }
