(* Exercice 1 *)


(* Cela renvoit 2 pour les 2 cas.*)



(* Exercice 2 *)

(* Le premier truc renvoit 4 *)


(* Le second renvoit 0 *)


(* Exercice 3 *)


let g n f = n + (f 12);;


let nique_ta_mere x w = (int_of_float x, int_of_float (w 0 0));; 

(* float -> (int->int->float) -> int*int *)
(* Exercice 4 *)


(* ('a -> 'b ) -> ('b -> 'c) -> 'a -> 'c *)

(* ('a -> int ) -> ('a -> int ) -> 'a -> int *)


(* Exercice 5 *)


(* ('a -> 'b ) * ('c ->'a) -> 'c -> 'b*)



(* Exercice 6 *)

(* ('a -> ('b -> 'c)) -> 'a -> 'b -> 'c *)
  
(* ('a -> 'b) -> ( 'c -> 'a) -> 'c  -> 'b *)

(* ('a -> 'b '-> 'c) -> 'a -> 'b -> 'c  *)

(* ('a -> 'b ) -> ('c -> ('a -> 'b) -> 'a) -> 'c -> 'b *)

(* ('a -> 'b -> 'c) -> 'a -> (('a -> 'b -> 'c) -> 'b) -> 'c *)


(* Exercice 7 *)


let implique p1 p2 = not p1 || p2;;



(* Exercice 8 *)


let delta u = function n -> u (n+1) - u n;;



(* Exercice 9 *)

let curry (f:('a*'b) -> 'c) = fun x y -> f (x,y);; 


let uncurry (f:'a -> 'b -> 'c) = function (x,y) -> f x y;;



(* Exercice 10 *)


(* Trop facile *)


(* Exercice 11 *)


let rec f p q = match p with
  | 0 -> q
  | x -> f (x-1) q + 1;;


let rec g p q = match p with
  | 0 -> q
  | x -> g (x-1) (q+1);;



(* Exercice 12 *)


let rec egyptienne p q = match p with
  | 1 -> q
  | x when x mod 2 = 0 -> egyptienne (p / 2) (2*q)
  | x -> egyptienne ((x-1)/2) (2*q) + q;;


let rec expo p q = match p with
  | 1 -> q
  | x when x mod 2 = 0 -> expo (p / 2) (q*q)
  | x -> expo ((x-1)/2) (q*q) *q ;;


