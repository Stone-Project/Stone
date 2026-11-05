// stone:job stone:math.smoothstep
// stone:function smoothstep_rs

#[no_mangle]
pub extern "C" fn smoothstep_rs(edge0: f64, edge1: f64, x: f64) -> f64 {
    let mut t = (x - edge0) / (edge1 - edge0);
    if t < 0.0 { t = 0.0; }
    if t > 1.0 { t = 1.0; }
    t * t * (3.0 - 2.0 * t)
}
