// stone:job stone:math.smootherstep_unclamped
// stone:function smootherstep_unclamped_rs

#[no_mangle]
pub extern "C" fn smootherstep_unclamped_rs(edge0: f64, edge1: f64, x: f64) -> f64 {
    if edge0 == edge1 { return f64::NAN; }
    let t = (x - edge0) / (edge1 - edge0);
    t * t * t * (t * (t * 6.0 - 15.0) + 10.0)
}
