// stone:job stone:math.smootherstep
// stone:function smootherstep_rs

#[no_mangle]
pub extern "C" fn smootherstep_rs(edge0: f64, edge1: f64, x: f64) -> f64 {
    let t = (x - edge0) / (edge1 - edge0);
    if t < 0.0 {
        0.0
    } else if t > 1.0 {
        1.0
    } else {
        t * t * t * (t * (t * 6.0 - 15.0) + 10.0)
    }
}
