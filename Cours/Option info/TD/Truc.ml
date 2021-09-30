type formule =
  |Var of int 
  |Neg of formule 
  |Conj of formule * formule
  |Disj of formule * formule


let hauteur phi =
  let rec f acc phi =
    match phi with
      |Var x -> acc
      |Conj (a,b) -> max (f (acc+1) a) (f (acc+1) b)
      |Disj (a,b) -> max (f (acc+1) a) (f (acc+1) b)
      |Neg x -> f (acc+1) x 
    in f 0 phi;;
      