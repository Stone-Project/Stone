// stone:job stone:math.shortest_arc_deg
// stone:function shortest_arc_deg_rs

#[no_mangle]
pub extern "C" fn shortest_arc_deg_rs(a: i32, b: i32) -> i32 {
    let mut d = (b - a).rem_euclid(360);
    if d > 180 {
        d -= 360;
    }
    d
}
