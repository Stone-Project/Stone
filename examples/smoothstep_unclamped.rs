// stone:job stone:math.smoothstep_unclamped
// stone:function smoothstep_unclamped_rs

#[no_mangle]
pub extern "C" fn smoothstep_unclamped_rs(edge0: f64, edge1: f64, x: f64) -> f64 {
    if edge0 == edge1 { return f64::NAN; }
    let t = (x - edge0) / (edge1 - edge0);
    t * t * (3.0 - 2.0 * t)
}
