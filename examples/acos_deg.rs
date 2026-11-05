// stone:job stone:math.acos_deg
// stone:function acos_deg_rs

#[no_mangle]
pub extern "C" fn acos_deg_rs(x: f64) -> f64 {
    if x < -1.0 || x > 1.0 { return f64::NAN; }
    x.acos().to_degrees()
}
