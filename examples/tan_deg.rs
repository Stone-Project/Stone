// stone:job stone:math.tan_deg
// stone:function tan_deg_rs

#[no_mangle]
pub extern "C" fn tan_deg_rs(d: f64) -> f64 {
    if d.rem_euclid(180.0) == 90.0 { return f64::NAN; }
    d.to_radians().tan()
}
