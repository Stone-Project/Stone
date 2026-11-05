// stone:job stone:math.clamp_angle_safe
// stone:function clamp_angle_safe_rs

#[no_mangle]
pub extern "C" fn clamp_angle_safe_rs(a: f64, lo: f64, hi: f64) -> f64 {
    if !(a.is_finite() && lo.is_finite() && hi.is_finite()) { return f64::NAN; }
    let span = (hi - lo).rem_euclid(360.0);
    let off = (a - lo).rem_euclid(360.0);
    if off <= span { return (lo + off).rem_euclid(360.0); }
    if off - span <= 360.0 - off { return hi.rem_euclid(360.0); }
    lo.rem_euclid(360.0)
}
