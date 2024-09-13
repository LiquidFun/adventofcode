let fuel x = x / 3 - 2;;
let rec fuel_of_fuel x = if x < 0 then 0 else x + (x |> fuel |> fuel_of_fuel);;

let rec collect_nums acc =
  try
    let line = input_line stdin in
    collect_nums ((line |> int_of_string |> fuel) :: acc)
  with End_of_file ->
    List.rev acc

let () = 
  let lines = collect_nums [] in 
  List.fold_left ( + ) 0 lines |> Printf.printf "%d\n";
  List.fold_left ( + ) 0 (List.map fuel_of_fuel lines) |> print_int