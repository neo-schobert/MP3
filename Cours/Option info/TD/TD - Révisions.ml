
let tab = [|1;2;3;4;5|]


(* Question 1 *)
let prod tab = 
  let s = ref 1 in
  for k = 0 to (Array.length tab)-1 do
    s := !s * tab.(k)
  done;
  !s;;

(* On a une boucle de n=len(tab) fois. La complexité est en O(n)*)


(* Question 2 *)
let quotient a b =
  let a= ref a in
  let quotient = ref 0 in
  while !a >= b do 
    a := !a - b;
    quotient := !quotient + 1
  done;
  !quotient;;

(* On a une boucle qui se fait a//b fois. Complexité en O(a//b) donc*)


(* Question 3 *)
let prod1 tab =
  let tab2 = Array.make (Array.length tab) 0 in
  let s = prod tab in
  for k = 0 to (Array.length tab) -1 do
    tab2.(k) <- quotient s tab.(k)
  done;
  tab2;;
 

(* Question 4 *)
(* Cette version calcul les termes du tableau 1 à 1 en le construisant à l'aide du constructeur ref *)

(* Chaque terme est calculé un à un. On a donc une boucle imbriquée dans une seconde. La complexité est en O(n^2) au lieu de O(n*s) pour la version 1. *)


(* Question 5 *)
(* 5.1 *)

(* Pour t=[|1;2;3;4;5|], p=[|1;2;6;24;120|] et s=[|120;120;60;20;5|] *)
(* 5.2 *)

let prod_pref_suff tab = 
  let n = Array.length tab in
  let p = Array.make n 0 and s = Array.make n 0 in
  p.(0)<- tab.(0);
  s.(n-1) <- tab.(n-1);
  for k = 1 to n-1 do
    p.(k) <- tab.(k)* p.(k-1);
    s.(n-k-1) <- s.(n-k) * tab.(n-k-1);
  done;
  (p,s);;

(* 5.3 *)

let prod3 tab =
  let n= Array.length tab in
  let tab2= Array.make n 0 in
  let (p,s)=prod_pref_suff tab in
  tab2.(0) <- s.(1);
  tab2.(n-1) <- p.(n-2);
  for k = 1 to n-2 do 
    tab2.(k) <- p.(k-1)*s.(k+1);
  done;
  tab2;;

(* 5.4 *)

(* Cette dernière fonction n'utilise construit d'abord deux tableaux préfixe et suffixe en O(n),
puis à partir de ces tableaux, forme le tableau voulu comme dans prod1 ou prod2.
Sa complexité est moindre car dans le calcul de préfixe et suffixe, on calcul chaque terme à partir
d'un précédent déjà enregistré. Cela ressemble au principe de programmation dynamique.
La complexité ici est évaluée en O(n). *)


(* Exercice 2 *)

type 'a arbre_binaire = Nil | Noeud of 'a * 'a arbre_binaire * 'a arbre_binaire;;


(* Question 1 *)
let rec is_in ett arbre =
  match arbre with
  | Nil -> false
  | Noeud(el,g,d) when el <= ett -> (el=ett) || (is_in ett d);
  | Noeud(el,g,d) -> (is_in ett g);
;;

(* Est en O(longueur de l'arbre) au maximum *)

(* Question 2 *)
let rec min_key = function
| Nil -> failwith "Error"
|Noeud(el,Nil,_) -> el
|Noeud(_,g,_) -> min_key g;;

  let rec max_key =function
  | Nil -> failwith "Error"
  | Noeud(el,_,Nil) -> el
  | Noeud(_,_,d) -> max_key d;;
  

(* Question 3 *)

let arbre = Noeud(5,
Noeud(2,
Noeud(1,Nil,Nil)
,Noeud(4,Noeud(3,Nil,Nil),Nil)),
Noeud(7,Noeud(6,Nil,Nil),Nil));;


(* Exercice 3 *)

(* Question 1 *)






(* Question 2 *)

